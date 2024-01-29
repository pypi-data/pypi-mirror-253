import argparse
import json
from os import PathLike
from codeGen.model import DecoderBase, make_model
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
)

from utils import get_human_eval_cleaned_doc, get_mbpp, get_humaneval_cs, get_humaneval_cpp, get_humaneval_java, get_lambda1, get_lambda2
from src.methods.demo_mutate import DemoMutation
from src.methods.description_mute import CharacterMutation, TokenMutation
from src.methods.semantic_mute import OutputTypeMutation,OutputValueMutation
# from src.methods.func_name import FuncNameMutation
from src.methods.sytanx_mute import CommentMutation, InsertLineMutation

import os


def get_dataset(dataset):
    if dataset == 'humaneval':
        return get_human_eval_cleaned_doc()  # 传递相应的参数
    elif dataset == 'mbpp':
        return get_mbpp()  # 传递相应的参数
    elif dataset == 'humaneval_cs':
        return get_humaneval_cs()  # 传递相应的参数
    elif dataset == 'humaneval_cpp':
        return get_humaneval_cpp()  # 传递相应的参数    
    elif dataset == 'humaneval_java':
        return get_humaneval_java()  # 传递相应的参数
    elif dataset == 'lambda1':
        return get_lambda1()  # 传递相应的参数
    elif dataset == 'lambda2':
        return get_lambda2()  # 传递相应的参数

    else:
        raise ValueError('Invalid param')


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
            # log = f"Codegen: {p_name} @ {model}"
            log = f"Codegen: {task_id} @ {model}"
            n_existing = 0

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

            elif args.construct_prompt == 'output_mutation':
                methods = OutputTypeMutation(task['prompt'], task['tests'], task['entry_point'])
                is_success, new_prompt, new_test, src_type, tgt_type, op = methods.mutate(task['language'])
                prompt = new_prompt
                if is_success == False:
                    continue
                #print(new_prompt)

                #task['prompt'] = new_prompt
                task['tests'] = new_test
            elif args.construct_prompt == 'output_v_mutation':
                methods = OutputValueMutation(task['prompt'], task['tests'], task['entry_point'])
                is_success, new_prompt, new_test, src_type, tgt_type, op = methods.mutate(task['language'])
                prompt = new_prompt
                if is_success == False:
                    continue
                task['tests'] = new_test

            elif args.construct_prompt == "func_name":
                methods = FuncNameMutation(task['prompt'], task['tests'], task['entry_point'])
                prompt, entry_point,new_test = methods.mutate(task['language'])
                task['tests'] = new_test
            elif args.construct_prompt == 'insert_line':
                methods = InsertLineMutation(task['prompt'], task['tests'], task['entry_point'])
                prompt = methods.mutate(task['language'])
            elif args.construct_prompt == 'comment':
                methods = CommentMutation(task['prompt'], task['tests'], task['entry_point'])
                prompt = methods.mutate(task['language'])

            # 将prompt保存
            with open(os.path.join(workdir, task_id, "prompt.txt"), "w") as f:
                f.write(str(prompt))
            if args.dataset in ['lambda1','lambda2']:
                result = {'name': task['id'], 'language': 'py', 'prompt': prompt, 'tests': task['tests'],
                        'completions': []}
            else:
                if args.construct_prompt in ['output_mutation','output_v_mutation']:
                    result = {'name': task['name'], 'language': task['language'], 'prompt': prompt, 'tests': task['tests'],
                        'completions': [], "stop_tokens": task['stop_tokens'], 'tokens': [], 'softmax': [],'is_sucess':is_success,"src_type":src_type,"tgt_type":tgt_type}
                else:
                    result = {'name': task['name'], 'language': task['language'], 'prompt': prompt, 'tests': task['tests'],
                            'completions': [], "stop_tokens": task['stop_tokens'], 'tokens': [], 'softmax': []}


            if args.resume:
                # count existing .py files
                n_existing = len(
                    [
                        f
                        for f in os.listdir(os.path.join(workdir, task_id))
                        if f.endswith(f".{task['language']}")
                    ]
                )
                if n_existing > 0:
                    log += f" (resuming from {n_existing})"

            nsamples = args.n_samples - n_existing
            p.console.print(log)

            sidx = args.n_samples - nsamples
            while sidx < args.n_samples:
                # stop_token(task['language'])
                if(args.model in {"chatgpt", "gpt-4"}):
                    outputs = model.codegen(
                        prompt,
                        do_sample=not args.greedy,
                        num_samples=args.n_samples - sidx,
                    )
                else:
                    outputs, tokens, logprobs = model.codegen(
                        prompt,
                        do_sample=not args.greedy,
                        num_samples=args.n_samples - sidx,
                    )
                    # result['tokens'].append(tokens)
                    # result['softmax'].append(logprobs)
                for impl in outputs:
                    try:
                        with open(
                                # os.path.join(workdir, task_id, f"{sidx}.{task['language']}"),
                                os.path.join(workdir, task_id, f"{sidx}.py"),
                                "w",
                                encoding="utf-8",
                        ) as f:
                            if args.model in {"chatgpt", "gpt-4"}:
                                f.write(impl + '\n' + task['tests'])
                                result['completions'].append(impl)
                            else:
                                f.write(prompt + impl + '\n' + task['tests'])
                                result['completions'].append(impl)
                    except UnicodeEncodeError:
                        continue
                    sidx += 1
            jsonpath = os.path.join(workdir, task_id, f"{task_id}.json")
            if not os.path.exists(jsonpath):
                with open(
                        jsonpath,
                        "w",
                        encoding="utf-8",
                ) as f:
                    json.dump(result, f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="incoder-1b", type=str)
    parser.add_argument("--bs", default=1, type=int)
    parser.add_argument("--temperature", default=0.7, type=float)
    parser.add_argument("--construct_prompt", default="output_mutation", type=str)
    parser.add_argument("--dataset", default="humaneval", type=str)
    parser.add_argument("--root", default="./workdir/codegen", type=str)
    parser.add_argument("--n_samples", default=100, type=int)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--greedy", action="store_true")
    parser.add_argument("--repeat_num", default=0, type=int)
    # "--resume"
    # 如果设置了这个参数，则会从中断的任务处恢复，否则就从头开始执行任务。
    # 如果命令行中使用了"–resume"参数，Python程序将接收到一个名为"resume"的True值。如果未使用该参数，则变量"resume"的值将为False。
    # "–-greedy"
    # 参数的作用是控制生成代码的策略方式。当使用”–greedy"
    # 参数时，程序使用
    # "greedy decoding"
    # 算法生成答案，即总是选择生成概率最高的单词。当未使用
    # "–greedy"
    # 参数时，程序将使用sampling
    # decoding算法，在模型的输出概率分布中进行随机采样来生成输出。

    args = parser.parse_args()

    if args.dataset not in ["humaneval", "humaneval_cs", "humaneval_cpp", "humaneval_java", "mbpp", "lambda1", "lambda2"]:
        raise NotImplementedError("Unsupported dataset: {}".format(args.dataset))

    if args.construct_prompt not in ["base", "add_demo", "del_demo", "rep_demo", "char_mutation", "token_mutation","output_mutation","output_v_mutation","func_name","insert_line","comment"]:
        raise NotImplementedError(
            "Unsupported contract usage: {}".format(args.construct_prompt)
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
    if args.repeat_num == 0:
        workdir = os.path.join(
            args.root,
            args.dataset,
            args.construct_prompt,
            args.model
            + f"_temp_{args.temperature}"
            ,
        )
    else:
        workdir = os.path.join(
            args.root,
            args.dataset,
            args.construct_prompt,
            args.model
            + f"_temp_{args.temperature}"
            + f"_repeat_{args.repeat_num}"
            ,
        )
    os.makedirs(workdir, exist_ok=True)

    with open(os.path.join(workdir, "args.txt"), "w") as f:
        f.write(str(args))

    code_generate(args, workdir=workdir, model=model)


if __name__ == "__main__":
    main()