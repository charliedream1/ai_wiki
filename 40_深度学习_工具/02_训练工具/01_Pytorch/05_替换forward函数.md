```python
import types

layer.gate.forward = types.MethodType(
    forward_topk_balanced_noisy_gate_with_random_expert_selection, layer.gate
)

def forward_topk_balanced_noisy_gate_with_random_expert_selection(self, x):
    # fmt: off
    batch_size = x.shape[0]

    logits = torch.rand((batch_size, self.num_experts), device=x.device, dtype=x.dtype)
    top_logits, top_indices = logits.topk(min(self.num_selects + 1, self.num_experts), dim=1)  # 选择并排序前k+1个权重
    top_k_logits = top_logits[:, :self.num_selects]
    top_k_indices = top_indices[:, :self.num_selects]
    top_k_scores = self.softmax(top_k_logits)

    # top_k_indices = torch.stack([torch.randperm(self.num_experts, device=x.device)[:self.num_selects] for i in range(batch_size)], dim=0)
    # top_k_scores = torch.sort(self.softmax(torch.rand_like(top_k_indices, dtype=x.dtype)), dim=1, descending=True)[0]

    return {
        "topK_indices": top_k_indices,
        "topK_scores": top_k_scores,
        "balance_loss": None,
        "load": None,
        "importance": None,
    }
    # fmt: on
```