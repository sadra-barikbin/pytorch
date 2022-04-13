#pragma once

#include <torch/csrc/lazy/ts_backend/ts_node.h>

namespace torch {
namespace lazy {

class TORCH_API NarrowViewUpdate : public TsNode {
 public:
  NarrowViewUpdate(
      const Value& input,
      const Value& source,
      c10::ArrayRef<int64_t> base_indices);

  bool Equal(
      const Value& input,
      const Value& source,
      c10::ArrayRef<int64_t> base_indices) const {
    size_t i = 0;
    return (
        operand(i++) == input && operand(i++) == source &&
        base_indices_ == base_indices);
  }

  std::string ToString() const override;

  const std::vector<int64_t>& base_indices() const {
    return base_indices_;
  }

 private:
  std::vector<int64_t> base_indices_;
};

} // namespace lazy
} // namespace torch
