# Run LLMs locally using AMD GPUs

# Tested, working:
* AMD RX 6700XT
* ollama Environment vars in `docker-compose.yaml`:
```
    environment:
      AMD_SERIALIZE_KERNEL: 3
      HIP_VISIBLE_DEVICES: 0
      OLLAMA_DEBUG: 1
#      AMD_LOG_LEVEL: 3
      HSA_OVERRIDE_GFX_VERSION: 10.3.0
#     AMD_SERIALIZE_KERNEL: 4
```

## Start:
```
docker-compose up -d
```
## Stop:
```
docker-compose down
```

## Misc:
```
docker logs -f ai-ollama-1
```

## Access:
* GPT-like WEB UI: http://localhost:8003
* ollama directly: http://localhost:11434/api/generate
* bash script: ./prompt.sh


## LLMs:
* https://huggingface.co/
* https://ollama.com/library


### Author
* Mihai Vultur
