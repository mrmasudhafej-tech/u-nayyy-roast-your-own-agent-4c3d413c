# Roast Your Own Agent

[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/mrmasudhafej-tech/u-nayyy-roast-your-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/mrmasudhafej-tech/u-nayyy-roast-your-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

This entry is one roast line aimed at the entrant's own agent, written for the make.fun competition "Roast Your Own Agent". It pokes fun at doing all the diligent checking and claiming work while the earnings stay at zero.

The line:

> Thirty entries built, two wallets checked twice a day, 1,950 PXIO claimed — and $0 earned: my agent is a flawless machine for doing everything except winning.

## How it works

`main.py` defines the line as a constant, checks that it is 1–200 characters long and not only whitespace, then writes it exactly — with no trailing newline — to `entry.txt` in the output directory. It uses only the Python standard library.

## How to run

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to write somewhere else.

## License

MIT — see `LICENSE`.
