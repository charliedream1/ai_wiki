import torch
from torch.nn import CrossEntropyLoss

"""来源CSDN上的一个代码，实测有效"""


def cal_ppl(sens, model, tokenizer):
    tokenizer.pad_token = tokenizer.convert_ids_to_tokens(151643)
    inputs = tokenizer(sens, return_tensors="pt", padding=True)
    inputs = inputs.to(model.device)

    bs, sl = inputs['input_ids'].size()
    outputs = model(**inputs.data, labels=inputs['input_ids'])
    logits = outputs[1]

    # Shift so that tokens < n predict n
    shift_logits = logits[:, :-1, :].contiguous()
    shift_labels = inputs['input_ids'][:, 1:].contiguous()
    shift_attentions = inputs['attention_mask'][:, 1:].contiguous()
    # Flatten the tokens
    loss_fct = CrossEntropyLoss(ignore_index=0, reduction="none")
    loss = loss_fct(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1)).detach().reshape(bs, -1)
    mean_loss = loss.sum(1) / shift_attentions.sum(1)
    ppl = torch.exp(mean_loss).detach().float().cpu().numpy().tolist()
    return ppl
