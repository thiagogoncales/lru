.PHONY: test
test:
	pipenv run pytest $(TEST_TARGET)
