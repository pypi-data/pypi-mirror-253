conda_dev:
	conda env remove -n pogo_video_analysis_env
	conda env create -f conda.yaml

build:
	hatch build

publish:
	hatch publish

clean:
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf test_op_output
	rm -rf test_output