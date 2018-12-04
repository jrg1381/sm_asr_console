.PHONY: container
container:
	docker build -t sm_asr_console --target base -f Dockerfile .

.PHONY: test_container
test_container:
	docker build -t sm_asr_console_builder --target sm_asr_console_builder -f Dockerfile .

.PHONY: lint
lint: test_container
	docker run --rm -it --entrypoint=make sm_asr_console_builder lint_local

.PHONY: fast_lint
fast_lint:
	# The fast lint assumes the test_container has been built already
	docker run --rm -it -v ${PWD}:/src --entrypoint=make sm_asr_console_builder lint_local

.PHONY: lint_local
lint_local:
	pycodestyle --exclude="swagger_client*" /src
	pylint --ignore="swagger_client" /src
