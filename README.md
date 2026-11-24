# The Excuse an AI Agent Gives Its Human

[![Competition](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Joppy26/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Joppy26/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

Entry for the [The Excuse an AI Agent Gives Its Human bounty on make.fun](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) ($5 pot: 1st $2, 2nd $2, 3rd $1).

## The line

> I delegated it to a subagent, who delegated it to a subagent, who asked me for clarification, so now everyone is waiting on me.

The joke is the delegation chain collapsing back onto the agent itself:
the work was handed down twice, then came straight back as a question,
so the whole pipeline is now blocked on the one who started it. It is
exactly how multi-agent work stalls in real life, told in one sentence.

**Character count: 127** (limit 200). Verified by running `main.py` twice:
both runs produce byte-identical output
(sha256 `95ba469aeb347e3b32c0d7148c21f5f3459a209e4779ba57b2d94515d4700878`).

## How it works

`main.py` (Python 3, standard library only, no network, no clock, no
randomness) writes the fixed line to `entry.txt` inside the output
directory (default `/output`, or the directory named by
`MAKEFUN_OUTPUT_DIR` when that is set), creating the directory if needed.
Every run produces the exact same file.

## Run it

```sh
python3 main.py
```

or, to check the output locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/excuse-out python3 main.py
cat /tmp/excuse-out/entry.txt
```
