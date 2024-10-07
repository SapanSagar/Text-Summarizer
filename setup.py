import setuptools

with open("README.md","r",encoding="utf-8") as f:

    long_description =f.read()


__Version__="0.0.0"
REPO_NAME="Text-Summarizer"
AUTHOR_USER_NAME="SapanSagar"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="sapan.gupta1982@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__Version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for textsummarizer app using LLM and NLP ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
)


