#!/bin/bash

params=$@

curl http://localhost:11434/api/generate \
--data @- << EOF
{
  "model": "deepseek-r1:8b",
  "prompt":"${params}",
  "stream": false
}
EOF
