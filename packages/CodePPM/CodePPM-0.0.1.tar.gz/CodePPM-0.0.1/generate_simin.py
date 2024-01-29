import argparse
import json
import torch
from os import PathLike
from codeGen.model import DecoderBase, make_model
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
)

from utils import get_dataset
from src.methods.demo_mutate import DemoMutation
from src.methods.description_mute import CharacterMutation, TokenMutation


import os


def solve_problem(p, args, workdir: PathLike, model: DecoderBase, task_id, task):
    # log = f"Codegen: {p_name} @ {model}"
    log = f"Codegen: {task_id} @ {model}"
    n_existing = 0
    meta_save_path = os.path.join(workdir, task_id, f"{task_id}.tar")

    # 根据baseline构建prompt
    if args.construct_prompt == "base":
        prompt = task["prompt"]
    elif args.construct_prompt == "add_demo":
        methods = DemoMutation(task['prompt'], task['tests'], task['entry_point'])
        prompt = methods.add_demo(task['language'])
    elif args.construct_prompt == "del_demo":
        methods = DemoMutation(task['prompt'], task['tests'], task['entry_point'])
        prompt = methods.del_demo(task['language'])
    elif args.construct_prompt == "rep_demo":
        methods = DemoMutation(task['prompt'], task['tests'], task['entry_point'])
        prompt = methods.rep_demo(task['language'])
    elif args.construct_prompt == "char_mutation":
        methods = CharacterMutation(task['prompt'], task['tests'], task['entry_point'])
        prompt = methods.mutate(task['language'])
    elif args.construct_prompt == "token_mutation":
        methods = TokenMutation(task['prompt'], task['tests'], task['entry_point'])

        prompt = methods.mutate(task['language'])

    # 将prompt保存
    with open(os.path.join(workdir, task_id, "prompt.txt"), "w") as f:
        f.write(str(prompt))

    result = {
        'name': task['name'], 'language': task['language'],
        'prompt': task['prompt'], 'tests': task['tests'],
        'completions': [], "tokens": [], "logprobs": [], "code": [],
        "stop_tokens": task['stop_tokens']
    }

    if args.resume:
        # count existing .py files
        result = torch.load(meta_save_path)
        n_existing = len(result['completions'])
        if n_existing > 0:
            log += f" (resuming from {n_existing})"

    nsamples = args.n_samples - n_existing
    p.console.print(log)

    sidx = args.n_samples - nsamples
    while sidx < args.n_samples:
        # stop_token(task['language'])
        outputs, tokens, logprobs = model.codegen(
            prompt,
            do_sample=not args.greedy,
            num_samples=args.n_samples - sidx,
        )
        for impl, token, logprob in zip(outputs, tokens, logprobs):
            try:
                with open(
                        os.path.join(workdir, task_id, f"{sidx}.{task['language']}"),
                        "w",
                        encoding="utf-8",
                ) as f:
                    if args.model in {"chatgpt", "gpt-4"}:
                        f.write(impl)
                    else:
                        f.write(prompt + impl + task['tests'])

                        result['code'].append(prompt + impl + task['tests'])
                        result['completions'].append(impl)
                        result["tokens"].append(token)
                        result["logprobs"].append(logprob)

            except UnicodeEncodeError:
                continue
            sidx += 1

        torch.save(result, meta_save_path)
    torch.save(result, meta_save_path)


def code_generate(args, workdir: PathLike, model: DecoderBase):
    # 该函数的作用是生成代码。它接受三个参数：args（命令行参数）、workdir（工作目录的路径）和model（模型对象）。

    # 显示进度条和时间
    with Progress(
        TextColumn(
            f"{args.dataset} •" + "[progress.percentage]{task.percentage:>3.0f}%"
        ),
        BarColumn(),
        MofNCompleteColumn(),
        TextColumn("•"),
        TimeElapsedColumn(),
    ) as p:
        for task_id, task in p.track(get_dataset(args.dataset).items()):
            # 任务id中的"/“替换成了”_"
            # p_name = task_id.replace("/", "_")
            os.makedirs(os.path.join(workdir, task_id), exist_ok=True)
            #try:
            solve_problem(p, args, workdir, model, task_id, task)
            #except:
            #    log = f"Codegen: {task_id} @ {model} Error"
            #    p.console.print(log)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="codegen-2b", type=str)
    parser.add_argument("--bs", default=1, type=int)
    parser.add_argument("--temperature", default=0.7, type=float)
    parser.add_argument("--construct_prompt", default="char_mutation", type=str)
    parser.add_argument("--dataset", default="humaneval", type=str)
    parser.add_argument("--root", default="./workdir/codegen", type=str)
    parser.add_argument("--n_samples", default=200, type=int)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--greedy", action="store_true")
    # "--resume"
    # 如果设置了这个参数，则会从中断的任务处恢复，否则就从头开始执行任务。
    # 如果命令行中使用了"–resume"参数，Python程序将接收到一个名为"resume"的True值。如果未使用该参数，则变量"resume"的值将为False。
    # "–greedy"
    # 参数的作用是控制生成代码的策略方式。当使用”–greedy"
    # 参数时，程序使用
    # "greedy decoding"
    # 算法生成答案，即总是选择生成概率最高的单词。当未使用
    # "–greedy"
    # 参数时，程序将使用sampling
    # decoding算法，在模型的输出概率分布中进行随机采样来生成输出。

    args = parser.parse_args()

    if args.dataset not in ["humaneval","humaneval_cs","humaneval_cpp","humaneval_java"]:
        raise NotImplementedError("Unsupported dataset: {}".format(args.dataset))

    if args.construct_prompt not in ["base", "add_demo", "del_demo", "rep_demo", "char_mutation", "token_mutation"]:
        raise NotImplementedError(
            "Unsupported contract usage: {}".format(args.constract_prompt)
        )

    # 当args.greedy为True时，代码中只允许使用temperature=0、batch_size=1和n_samples=1。
    # 这意味着，在greedy decoding模式下，只能生成一个单一、确定性的结果。
    # 如果用户尝试在命令行中设置了不允许的参数值，程序将引发异常并提示错误消息。
    if args.greedy and (args.temperature != 0 or args.bs != 1 or args.n_samples != 1):
        raise ValueError(
            f"Greedy decoding is only supported with temperature({args.temperature}) = 0, batch_size({args.bs}) = 1"
            f" and n_samples({args.n_samples}) = 1"
        )

    # Make project dir
    os.makedirs(args.root, exist_ok=True)
    # Make dataset dir
    os.makedirs(os.path.join(args.root, args.dataset), exist_ok=True)
    # Make dir for codes generated by each model
    args.model = args.model.lower()
    model = make_model(
        name=args.model, batch_size=args.bs, temperature=args.temperature
    )
    workdir = os.path.join(
        args.root,
        args.dataset,
        args.construct_prompt,
        args.model
        + f"_temp_{args.temperature}"
        ,
    )
    os.makedirs(workdir, exist_ok=True)

    with open(os.path.join(workdir, "args.txt"), "w") as f:
        f.write(str(args))

    code_generate(args, workdir=workdir, model=model)


if __name__ == "__main__":
    main()
