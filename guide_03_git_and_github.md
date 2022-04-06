## Getting started with Git and GitHub

### What is Git? What is GitHub

![git and github](https://i.imgur.com/G3ow8WV.jpg)

Git is an open-source version control system that was started by Linus Torvalds—the same person who created Linux. Git is similar to other version control systems—Subversion, CVS, and Mercurial to name a few.

A repository (usually abbreviated to “repo”) is a location where all the files for a particular project are stored. Each project has its own repo, and you can access it with a unique URL.

GitHub is a web-based version-control and collaboration platform for software developers. Microsoft, the biggest single contributor to GitHub, initiated an acquisition of GitHub for $7.5 billion in June, 2018.

_GitHub can be thought of as a serious social networking site for software developers. Members can follow each other, rate each other's work, receive updates for specific projects and communicate publicly or privately._

<hr/>

### Basic Git Commands

- #### Forking a repo

A fork is a copy of a repository. Forking a repository allows to freely experiment with changes without affecting the original project.

- #### Cloning a repo

Cloning is a process of creating an identical copy of a Git Remote Repository to the local machine.

```
git clone https://github.com/trashvin/python-gamedev-2021.git
```

- ####  Working with codes

adding codes to the repo

```
git add .
```

commiting changes

```
git commit -m "initial commit"
```

pushing changes

```
get push
```

pulling changes

```
git pull
```
- #### Miscellaneous commands
```
git config --global user.name "Your Name"
git config --global user.email "youremail@yourdomain.com"
```
<hr/>
<div style="text-align: right"> 
<a href='/learning-basic-python-and-flask/guide_02_debugging_python_vscode'>Previous</a> | <a href = 'https://trashvin.github.io/learning-basic-python-and-flask/'>Home</a>
</div>
