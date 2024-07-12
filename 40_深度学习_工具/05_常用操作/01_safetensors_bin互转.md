You will get .safetensors format model if you save model by below code:

```python
model.save_pretrained('folder/')
```

And you will get .bin format model if you save model by below code:

```python
torch.save(model.state_dict(), 'folder/pytorch_model.bin'.format(epoch))
```

# 参考

[1] https://stackoverflow.com/questions/77708996/how-to-convert-model-safetensor-to-pytorch-model-bin