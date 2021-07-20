# Coading convention

--------

# [Naming conventions and recipes related to packaging](https://www.python.org/dev/peps/pep-0423/)


## Overview

* make sure your project name is unique, i.e. avoid duplicates:
    * use top-level namespace for ownership,
    * check for name availability,
    * register names with PyPI.

* make it easy to discover and remember your project:
    * use as much memorable names as possible,
    * use as much meaningful names as possible,
    * use other packaging metadata.

* avoid deep nesting. Flat things are easier to use and remember than nested ones:
    * one or two namespace levels are recommended, because they are almost always enough.
    * even if not recommended, three levels are, de facto, a common case.
    * in most cases, you should not need more than three levels.

## Top-level namespace relates to code ownership(code/package kasle maintain gardai x tyo clear define vayasi authentic package ho vanni tha hunxa)

* an individual. Example: gp.fileupload [7] is owned and maintained by Gael Pasgrimaud.
* an organization. Examples:
    * zest.releaser [8] is owned and maintained by Zest Software.
    * Django [9] is owned and maintained by the Django Software Foundation.
* a group or community. Example: sphinx [10] is maintained by developers of the Sphinx project, not only by its author, Georg Brandl.
* a group or community related to another package. Example: collective.recaptcha [12] is owned by its author: David Glick, Groundwire. But the "collective" namespace is owned by Plone community.

## Use a single name

Distribute only one package (or only one module) per project, and use package (or module) name as project name.


* It avoids possible confusion between project name and distributed package or module name.

* It makes the name consistent.

* It is explicit: when one sees project name, he guesses package/module name, and vice versa.

* It also limits implicit clashes between package/module names. By using a single name, when you register a project name to PyPI [11], you also perform a basic package/module name availability verification.

As an example, pipeline [13], python-pipeline [14] and django-pipeline [15] all distribute a package or module called "pipeline". So installing two of them leads to errors. This issue wouldn't have occurred if these distributions used a single name.

Yes:

    * Package name: "kheops.pyramid", i.e. import kheops.pyramid
    * Project name: "kheops.pyramid", i.e. pip install kheops.pyramid
No:

    * Package name: "kheops"
    * Project name: "KheopsPyramid"




## Follow PEP 8 for syntax of package and module names

Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.


# [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)
