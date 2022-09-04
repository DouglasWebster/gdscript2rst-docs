.. gdscript2rst-docs documentation master file, created by
   sphinx-quickstart on Sat Sep  3 12:12:14 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

###########################
gdscript2rest documentation
###########################

Introduction
============

The utility gdscript2rest was written so that gdscript API comments can be converted to
reStructuredText format for including in documentation.

Whilst the utility function is to generate reStructuredText files the main focus was to
include these files in a Sphinx document.  This documentation will detail the procedures
and tools required to complete this task.

Requirements
============

.. list-table:: Requirements
    :widths: 20 20
    :header-rows: 1
    :class: tight-table

    * - Item
      - Function
    * - python 3.7+
      - Build environment
    * - Godot 3.2
      - What it's all about
    * - gdscript2rest
      - This utility
    * - godot-api-refs
      - Creates a cross reference Json file - enables linking to the Godot API in user documentation.
    * - Sphinx
      - The python package for creating documentation
    * - sphinx-rtd-theme
      - The theme that gives the documentation a similar look and feel as the Godot documentation
    * - sphinx-notfound-page
      - Used to replace the horrible standard not found page for bad(?) links.
    * - sphinx-tabs
      - Enables tab creation in the document (optional).
    * - Pygments
      - Gives syntax highlighting for code snippets in the document.
    * - An IDE
      - A Tool for managing the document creation.  This documentation is based on VSCode but should be readily convertable to other IDE's

The following sections are provided to take you through the full setting up and creation of a document

  - Installation: Instruction on how to install the above requirements.
  - Creating Godot API's:  How to comment your Godot code so that the API's can be extracted
  - Setting up VSCode
  - Using gdscript2rest to create the reStructuredText files



.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:

.. toctree:: 
  :maxdepth: 2
  :hidden:
  :caption: Installation
  :name: sec-installation

  installation/index


