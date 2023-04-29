init:
	git clone --depth 1 https://github.com/scribble-service/java-skeleton.git
	rm -rf java-skeleton/.git
	cp -rf ./java-skeleton/. .
	rm -rf java-skeleton
	python3 setup.py