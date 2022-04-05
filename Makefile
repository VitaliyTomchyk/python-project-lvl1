setup: build publish package-install push

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run -u "\n" -p "\n"

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

push:
	git add .
	git commit -m 'my commit'
	git push

lint:
	poetry run flake8 brain_games
