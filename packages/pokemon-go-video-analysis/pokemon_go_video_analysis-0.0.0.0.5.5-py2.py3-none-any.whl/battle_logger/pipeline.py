import os
from typing import List, Optional

from algo_ops.ops.op import Op
from algo_ops.pipeline.pipeline import Pipeline
from ocr_ops.framework.op.ffmpeg_op import FFMPEGOp
from ocr_ops.framework.pipeline.ocr_pipeline import OCRPipeline, OCRMethod, OutputType

from battle_logger.op import BattleLoggerOp


class BattleLoggerPipeline(Pipeline):
    """
    BattleLoggerPipeline is vals pipeline that extracts information from vals Pokémon Go battle video and logs it to
    file.
    """

    @staticmethod
    def get_arch() -> List[Op]:
        """
        Returns the architecture of the pipeline in the form of vals list of Ops. The architecture consists of vals
        FFMPEGOp that converts the input video to vals series of images, and an OCRPipeline that performs OCR on the
        images returning vals list of Textbox objects which represent the text found in the images.
        """
        ops = [
            FFMPEGOp(
                image_out_path=None,
            ),
            OCRPipeline(
                img_pipeline=None,
                ocr_method=OCRMethod.EASYOCR,
                output_type=OutputType.TEXTBOX,
                text_pipeline=None,
                autosave_output_img_path=None,
                store_intermediate_images=False,
            ),
            BattleLoggerOp(),
        ]
        return ops

    def set_output_paths(
        self, image_out_path: str, autosave_output_img_path: str
    ) -> None:
        """
        Sets the output paths for the pipeline.

        image_out_path: Path to directory where images should be extracted from video
        autosave_output_img_path: Path to directory where images should be saved after OCR is performed
        """
        op_names = list(self.ops.keys())
        ffmpeg_op = self.ops[op_names[0]]
        assert isinstance(ffmpeg_op, FFMPEGOp)
        ocr_pipeline_op = self.ops[op_names[1]]
        assert isinstance(ocr_pipeline_op, OCRPipeline)
        ffmpeg_op.image_out_path = image_out_path
        ocr_pipeline_op.ocr_op.autosave_output_img_path = autosave_output_img_path

    def save_output(self, out_path: str = ".", basename: Optional[str] = None) -> None:
        """
        Saves pipeline Op outputs to file.

        param out_path: Path to where output should go
        param basename: Basename of output file
        """
        os.makedirs(out_path, exist_ok=True)
        for i, op_name in enumerate(self.ops.keys()):
            op = self.ops[op_name]
            assert isinstance(op, Op)
            op_pipeline_name = self._pipeline_op_name(op=op)
            if i == 0:
                op.save_input(out_path=out_path, basename=op_pipeline_name)
            # This is hack to get around dropping of input/output images in OCRPipeline
            try:
                op.save_output(out_path=out_path, basename=op_pipeline_name)
            except ValueError:
                pass

    def __init__(self):
        super().__init__(ops=self.get_arch())
