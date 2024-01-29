import os

from battle_logger.op import BattleLoggerOp
from battle_logger.pipeline import BattleLoggerPipeline

if __name__ == "__main__":
    # paths
    input_path = "/home/borg1/Desktop/pogo_videos/az_recorder_20230321_152726.mp4"
    out_root = "test_output"

    # generate output paths
    image_out_path = os.path.join(out_root, "images")
    autosave_output_img_path = os.path.join(out_root, "ocr_images")

    # run pipeline
    pogo_pipeline = BattleLoggerPipeline()
    pogo_pipeline.set_output_paths(
        image_out_path=image_out_path, autosave_output_img_path=autosave_output_img_path
    )
    output = pogo_pipeline.exec(input_path)

    # save output to disk
    pogo_pipeline.save_output(out_path=out_root, basename="output")

    # save to file and check
    battle_logger_op = pogo_pipeline.find_ops_by_class(op_class=BattleLoggerOp)[0]
    battle_logger_op.save_input(out_path=out_root, basename="ocr_output")
