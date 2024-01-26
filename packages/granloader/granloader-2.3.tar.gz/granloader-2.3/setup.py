from setuptools import setup, find_packages

setup(
	name='granloader',
	version='2.3',
	packages=find_packages(),
	install_requires=[
		'yt-dlp',
		'ffmpeg-python'
	]
)