# CSU-Lunabotics-2024

Software team Lunabotics workspace

## Rules

Please follow this rules for a smooth usage of this git. (So you don't have problems with **Conner**)

### Branches

Create you own branch for any changes that you make. Use this command to create a new branch

`git checkout -b 'name_of_the_branch'`

> **Note:** If you push directly to main you owe the group a pizza

The syntax of the names of the branches will be your name and what you are working on separated by a `_` follow the example below:

`git checkout -b 'conner_crying'`

### Directories

Let's try to keep our git as clean as possible so it is easy for everyone to navigate through it.

If you are working with ROS put your packages inside the `src` directory.

If you are working on something not related to ROS, create a new folder with a title related on what you are working on.

---

## Help

Useful commands

- To see what branch you are working on:

`git branch`

- To move to a different branch:

`git checkout 'name_of_the_branch'`

- To update with the changes from the repo:

`git fetch`

- To get all the changes from the repo and update you home directory:

`git pull`

- To save you changes:

`git add [file]`

- To commit your changes:

`git commit -m "Description of what you are commiting"`

- To push all your changes:

`git push origin [branch name]`
