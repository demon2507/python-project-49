# Makefile
install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

publish:
	poetry publish --dry-run

package-install:
	uv tool install dist/*.whl
