title: Pro Tip - Pip Upgrade All Python Packages
author: Mike Grouchy
date: 2014-06-02
tags:
    - python
    - pip
    - packages

An open and ongoing [feature request](https://github.com/pypa/pip/issues/59) for PIP is to add an `upgrade-all` command to
PIP. Due to the lack of this feature a workaround is required. Enter Stackoverflow.

I have been using a variation of this particular command line trick for awhile,
but when starting writing this up I googled other solutions and [this](http://stackoverflow.com/a/3452888/2867) is one of the
nicest and most straightforward I have seen.

```shell
	pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U
```

So next time you want to upgrade all the packages in your virtualenv, this is a great
place to start. I have this set up as an alias to `pipup` in my [.zshrc](https://github.com/mgrouchy/dotfiles/blob/master/.zshalias#L31) for convenience.
