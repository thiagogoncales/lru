.PHONY: install
install:
	pipenv install

.PHONY: test
test:
	pipenv run pytest $(TEST_TARGET)
