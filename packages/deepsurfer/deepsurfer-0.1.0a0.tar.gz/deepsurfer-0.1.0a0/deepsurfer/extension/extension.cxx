#include <torch/extension.h>


at::Tensor NearestNeighbor(const at::Tensor&, const at::Tensor&,
                           const at::Tensor&, const at::Tensor&);

std::tuple<at::Tensor, at::Tensor> MarkSelfIntersectingFaces(const at::Tensor&, const at::Tensor&);


PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("nearest_neighbor", &NearestNeighbor);
    m.def("mark_self_intersecting_faces", &MarkSelfIntersectingFaces);
}
