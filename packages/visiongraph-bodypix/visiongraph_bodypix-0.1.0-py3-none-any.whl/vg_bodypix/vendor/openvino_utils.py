import openvino as ov


def update_constant(op, parameter_index: int, value: float):
    old_const = op.input_value(parameter_index).node
    const = ov.opset1.constant(value, ov.Type.f32)

    print(f"Updating constant {op.get_name()}[{parameter_index}] from {old_const.get_data()} to {const.get_data()}")

    op.set_argument(parameter_index, const.output(0))


def set_mask_score_threshold(model: ov.Model, mask_score_threshold: float):
    const = ov.runtime.opset1.constant(mask_score_threshold, ov.Type.f32)

    ops = [op for op in model.get_ops() if op.friendly_name == "mask_score_threshold_less"]
    for op in ops:
        for i, input_value in enumerate(op.input_values()):
            if input_value.node.friendly_name == "mask_score_threshold":
                op.set_argument(i, const.output(0))


def set_nms_parameters(model: ov.Model, score_threshold: float, iou_threshold: float):
    nms_ops = [op for op in model.get_ops() if op.get_type_name() == "NonMaxSuppression"]
    for op in nms_ops:
        update_constant(op, 3, iou_threshold)
        update_constant(op, 4, score_threshold)
