import click
import pathlib
from pathlib import Path
import time
import subprocess
import sys
import webbrowser

def error(message):
    click.secho("error: ", fg="red", bold=True, nl=False)
    click.secho(message)

def success(message):
    click.secho("success: ", fg="green", bold=True, nl=False)
    click.secho(message)

def info(message):
    click.secho("info: ", fg="blue", bold=True, nl=False)
    click.secho(message)

@click.group()
def cli():
    pass

def generate_doxyfile(project_name):
    return f"""# Doxyfile 1.9.6

#---------------------------------------------------------------------------
# Project related configuration options
#---------------------------------------------------------------------------
DOXYFILE_ENCODING      = UTF-8
PROJECT_NAME           = {project_name}
PROJECT_NUMBER         =
PROJECT_BRIEF          =
PROJECT_LOGO           =
OUTPUT_DIRECTORY       = ../docs
CREATE_SUBDIRS         = NO
CREATE_SUBDIRS_LEVEL   = 8
ALLOW_UNICODE_NAMES    = NO
OUTPUT_LANGUAGE        = English
BRIEF_MEMBER_DESC      = YES
REPEAT_BRIEF           = YES
ABBREVIATE_BRIEF       = "The $name class" \
                         "The $name widget" \
                         "The $name file" \
                         is \
                         provides \
                         specifies \
                         contains \
                         represents \
                         a \
                         an \
                         the
ALWAYS_DETAILED_SEC    = NO
INLINE_INHERITED_MEMB  = NO
FULL_PATH_NAMES        = YES
STRIP_FROM_PATH        =
STRIP_FROM_INC_PATH    =
SHORT_NAMES            = NO
JAVADOC_AUTOBRIEF      = NO
JAVADOC_BANNER         = NO
QT_AUTOBRIEF           = NO
MULTILINE_CPP_IS_BRIEF = NO
PYTHON_DOCSTRING       = YES
INHERIT_DOCS           = YES
SEPARATE_MEMBER_PAGES  = NO
TAB_SIZE               = 4
ALIASES                =
OPTIMIZE_OUTPUT_FOR_C  = NO
OPTIMIZE_OUTPUT_JAVA   = NO
OPTIMIZE_FOR_FORTRAN   = NO
OPTIMIZE_OUTPUT_VHDL   = NO
OPTIMIZE_OUTPUT_SLICE  = NO
EXTENSION_MAPPING      =
MARKDOWN_SUPPORT       = YES
TOC_INCLUDE_HEADINGS   = 5
AUTOLINK_SUPPORT       = YES
BUILTIN_STL_SUPPORT    = NO
CPP_CLI_SUPPORT        = NO
SIP_SUPPORT            = NO
IDL_PROPERTY_SUPPORT   = YES
DISTRIBUTE_GROUP_DOC   = NO
GROUP_NESTED_COMPOUNDS = NO
SUBGROUPING            = YES
INLINE_GROUPED_CLASSES = NO
INLINE_SIMPLE_STRUCTS  = NO
TYPEDEF_HIDES_STRUCT   = NO
LOOKUP_CACHE_SIZE      = 0
NUM_PROC_THREADS       = 1
#---------------------------------------------------------------------------
# Build related configuration options
#---------------------------------------------------------------------------
EXTRACT_ALL            = NO
EXTRACT_PRIVATE        = NO
EXTRACT_PRIV_VIRTUAL   = NO
EXTRACT_PACKAGE        = NO
EXTRACT_STATIC         = NO
EXTRACT_LOCAL_CLASSES  = YES
EXTRACT_LOCAL_METHODS  = NO
EXTRACT_ANON_NSPACES   = NO
RESOLVE_UNNAMED_PARAMS = YES
HIDE_UNDOC_MEMBERS     = NO
HIDE_UNDOC_CLASSES     = NO
HIDE_FRIEND_COMPOUNDS  = NO
HIDE_IN_BODY_DOCS      = NO
INTERNAL_DOCS          = NO
CASE_SENSE_NAMES       = SYSTEM
HIDE_SCOPE_NAMES       = NO
HIDE_COMPOUND_REFERENCE= NO
SHOW_HEADERFILE        = YES
SHOW_INCLUDE_FILES     = YES
SHOW_GROUPED_MEMB_INC  = NO
FORCE_LOCAL_INCLUDES   = NO
INLINE_INFO            = YES
SORT_MEMBER_DOCS       = YES
SORT_BRIEF_DOCS        = NO
SORT_MEMBERS_CTORS_1ST = NO
SORT_GROUP_NAMES       = NO
SORT_BY_SCOPE_NAME     = NO
STRICT_PROTO_MATCHING  = NO
GENERATE_TODOLIST      = YES
GENERATE_TESTLIST      = YES
GENERATE_BUGLIST       = YES
GENERATE_DEPRECATEDLIST= YES
ENABLED_SECTIONS       =
MAX_INITIALIZER_LINES  = 30
SHOW_USED_FILES        = YES
SHOW_FILES             = YES
SHOW_NAMESPACES        = YES
FILE_VERSION_FILTER    =
LAYOUT_FILE            =
CITE_BIB_FILES         =
#---------------------------------------------------------------------------
# Configuration options related to warning and progress messages
#---------------------------------------------------------------------------
QUIET                  = NO
WARNINGS               = YES
WARN_IF_UNDOCUMENTED   = YES
WARN_IF_DOC_ERROR      = YES
WARN_IF_INCOMPLETE_DOC = YES
WARN_NO_PARAMDOC       = NO
WARN_IF_UNDOC_ENUM_VAL = NO
WARN_AS_ERROR          = NO
WARN_FORMAT            = "$file:$line: $text"
WARN_LINE_FORMAT       = "at line $line of file $file"
WARN_LOGFILE           =
#---------------------------------------------------------------------------
# Configuration options related to the input files
#---------------------------------------------------------------------------
INPUT                  = ../src
INPUT_ENCODING         = UTF-8
INPUT_FILE_ENCODING    =
FILE_PATTERNS          = *.c \
                         *.cc \
                         *.cxx \
                         *.cpp \
                         *.c++ \
                         *.java \
                         *.ii \
                         *.ixx \
                         *.ipp \
                         *.i++ \
                         *.inl \
                         *.idl \
                         *.ddl \
                         *.odl \
                         *.h \
                         *.hh \
                         *.hxx \
                         *.hpp \
                         *.h++ \
                         *.l \
                         *.cs \
                         *.d \
                         *.php \
                         *.php4 \
                         *.php5 \
                         *.phtml \
                         *.inc \
                         *.m \
                         *.markdown \
                         *.md \
                         *.mm \
                         *.dox \
                         *.py \
                         *.pyw \
                         *.f90 \
                         *.f95 \
                         *.f03 \
                         *.f08 \
                         *.f18 \
                         *.f \
                         *.for \
                         *.vhd \
                         *.vhdl \
                         *.ucf \
                         *.qsf \
                         *.ice
RECURSIVE              = YES
EXCLUDE                =
EXCLUDE_SYMLINKS       = NO
EXCLUDE_PATTERNS       =
EXCLUDE_SYMBOLS        =
EXAMPLE_PATH           =
EXAMPLE_PATTERNS       = *
EXAMPLE_RECURSIVE      = NO
IMAGE_PATH             =
INPUT_FILTER           =
FILTER_PATTERNS        =
FILTER_SOURCE_FILES    = NO
FILTER_SOURCE_PATTERNS =
USE_MDFILE_AS_MAINPAGE =
FORTRAN_COMMENT_AFTER  = 72
#---------------------------------------------------------------------------
# Configuration options related to source browsing
#---------------------------------------------------------------------------
SOURCE_BROWSER         = NO
INLINE_SOURCES         = NO
STRIP_CODE_COMMENTS    = YES
REFERENCED_BY_RELATION = NO
REFERENCES_RELATION    = NO
REFERENCES_LINK_SOURCE = YES
SOURCE_TOOLTIPS        = YES
USE_HTAGS              = NO
VERBATIM_HEADERS       = YES
#---------------------------------------------------------------------------
# Configuration options related to the alphabetical class index
#---------------------------------------------------------------------------
ALPHABETICAL_INDEX     = YES
IGNORE_PREFIX          =
#---------------------------------------------------------------------------
# Configuration options related to the HTML output
#---------------------------------------------------------------------------
GENERATE_HTML          = YES
HTML_OUTPUT            = html
HTML_FILE_EXTENSION    = .html
HTML_HEADER            =
HTML_FOOTER            =
HTML_STYLESHEET        =
HTML_EXTRA_STYLESHEET  =
HTML_EXTRA_FILES       =
HTML_COLORSTYLE        = AUTO_LIGHT
HTML_COLORSTYLE_HUE    = 208
HTML_COLORSTYLE_SAT    = 217
HTML_COLORSTYLE_GAMMA  = 56
HTML_TIMESTAMP         = NO
HTML_DYNAMIC_MENUS     = YES
HTML_DYNAMIC_SECTIONS  = NO
HTML_INDEX_NUM_ENTRIES = 100
GENERATE_DOCSET        = NO
DOCSET_FEEDNAME        = "Doxygen generated docs"
DOCSET_FEEDURL         =
DOCSET_BUNDLE_ID       = org.doxygen.Project
DOCSET_PUBLISHER_ID    = org.doxygen.Publisher
DOCSET_PUBLISHER_NAME  = Publisher
GENERATE_HTMLHELP      = NO
CHM_FILE               =
HHC_LOCATION           =
GENERATE_CHI           = NO
CHM_INDEX_ENCODING     =
BINARY_TOC             = NO
TOC_EXPAND             = NO
GENERATE_QHP           = NO
QCH_FILE               =
QHP_NAMESPACE          = org.doxygen.Project
QHP_VIRTUAL_FOLDER     = doc
QHP_CUST_FILTER_NAME   =
QHP_CUST_FILTER_ATTRS  =
QHP_SECT_FILTER_ATTRS  =
QHG_LOCATION           =
GENERATE_ECLIPSEHELP   = NO
ECLIPSE_DOC_ID         = org.doxygen.Project
DISABLE_INDEX          = NO
GENERATE_TREEVIEW      = YES
FULL_SIDEBAR           = NO
ENUM_VALUES_PER_LINE   = 4
TREEVIEW_WIDTH         = 250
EXT_LINKS_IN_WINDOW    = NO
OBFUSCATE_EMAILS       = YES
HTML_FORMULA_FORMAT    = png
FORMULA_FONTSIZE       = 10
FORMULA_MACROFILE      =
USE_MATHJAX            = NO
MATHJAX_VERSION        = MathJax_2
MATHJAX_FORMAT         = HTML-CSS
MATHJAX_RELPATH        =
MATHJAX_EXTENSIONS     =
MATHJAX_CODEFILE       =
SEARCHENGINE           = YES
SERVER_BASED_SEARCH    = NO
EXTERNAL_SEARCH        = NO
SEARCHENGINE_URL       =
SEARCHDATA_FILE        = searchdata.xml
EXTERNAL_SEARCH_ID     =
EXTRA_SEARCH_MAPPINGS  =
#---------------------------------------------------------------------------
# Configuration options related to the LaTeX output
#---------------------------------------------------------------------------
GENERATE_LATEX         = NO
LATEX_OUTPUT           = latex
LATEX_CMD_NAME         =
MAKEINDEX_CMD_NAME     = makeindex
LATEX_MAKEINDEX_CMD    = makeindex
COMPACT_LATEX          = NO
PAPER_TYPE             = a4
EXTRA_PACKAGES         =
LATEX_HEADER           =
LATEX_FOOTER           =
LATEX_EXTRA_STYLESHEET =
LATEX_EXTRA_FILES      =
PDF_HYPERLINKS         = YES
USE_PDFLATEX           = YES
LATEX_BATCHMODE        = NO
LATEX_HIDE_INDICES     = NO
LATEX_BIB_STYLE        = plain
LATEX_TIMESTAMP        = NO
LATEX_EMOJI_DIRECTORY  =
#---------------------------------------------------------------------------
# Configuration options related to the RTF output
#---------------------------------------------------------------------------
GENERATE_RTF           = NO
RTF_OUTPUT             = rtf
COMPACT_RTF            = NO
RTF_HYPERLINKS         = NO
RTF_STYLESHEET_FILE    =
RTF_EXTENSIONS_FILE    =
#---------------------------------------------------------------------------
# Configuration options related to the man page output
#---------------------------------------------------------------------------
GENERATE_MAN           = NO
MAN_OUTPUT             = man
MAN_EXTENSION          = .3
MAN_SUBDIR             =
MAN_LINKS              = NO
#---------------------------------------------------------------------------
# Configuration options related to the XML output
#---------------------------------------------------------------------------
GENERATE_XML           = NO
XML_OUTPUT             = xml
XML_PROGRAMLISTING     = YES
XML_NS_MEMB_FILE_SCOPE = NO
#---------------------------------------------------------------------------
# Configuration options related to the DOCBOOK output
#---------------------------------------------------------------------------
GENERATE_DOCBOOK       = NO
DOCBOOK_OUTPUT         = docbook
#---------------------------------------------------------------------------
# Configuration options for the AutoGen Definitions output
#---------------------------------------------------------------------------
GENERATE_AUTOGEN_DEF   = NO
#---------------------------------------------------------------------------
# Configuration options related to Sqlite3 output
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# Configuration options related to the Perl module output
#---------------------------------------------------------------------------
GENERATE_PERLMOD       = NO
PERLMOD_LATEX          = NO
PERLMOD_PRETTY         = YES
PERLMOD_MAKEVAR_PREFIX =
#---------------------------------------------------------------------------
# Configuration options related to the preprocessor
#---------------------------------------------------------------------------
ENABLE_PREPROCESSING   = YES
MACRO_EXPANSION        = NO
EXPAND_ONLY_PREDEF     = NO
SEARCH_INCLUDES        = YES
INCLUDE_PATH           =
INCLUDE_FILE_PATTERNS  =
PREDEFINED             =
EXPAND_AS_DEFINED      =
SKIP_FUNCTION_MACROS   = YES
#---------------------------------------------------------------------------
# Configuration options related to external references
#---------------------------------------------------------------------------
TAGFILES               =
GENERATE_TAGFILE       =
ALLEXTERNALS           = NO
EXTERNAL_GROUPS        = YES
EXTERNAL_PAGES         = YES
#---------------------------------------------------------------------------
# Configuration options related to the dot tool
#---------------------------------------------------------------------------
DIA_PATH               =
HIDE_UNDOC_RELATIONS   = YES
HAVE_DOT               = NO
DOT_NUM_THREADS        = 0
DOT_COMMON_ATTR        = "fontname=Helvetica,fontsize=10"
DOT_EDGE_ATTR          = "labelfontname=Helvetica,labelfontsize=10"
DOT_NODE_ATTR          = "shape=box,height=0.2,width=0.4"
DOT_FONTPATH           =
CLASS_GRAPH            = YES
COLLABORATION_GRAPH    = YES
GROUP_GRAPHS           = YES
UML_LOOK               = NO
UML_LIMIT_NUM_FIELDS   = 10
DOT_UML_DETAILS        = NO
DOT_WRAP_THRESHOLD     = 17
TEMPLATE_RELATIONS     = NO
INCLUDE_GRAPH          = YES
INCLUDED_BY_GRAPH      = YES
CALL_GRAPH             = NO
CALLER_GRAPH           = NO
GRAPHICAL_HIERARCHY    = YES
DIRECTORY_GRAPH        = YES
DIR_GRAPH_MAX_DEPTH    = 1
DOT_IMAGE_FORMAT       = png
INTERACTIVE_SVG        = NO
DOT_PATH               =
DOTFILE_DIRS           =
MSCFILE_DIRS           =
DIAFILE_DIRS           =
PLANTUML_JAR_PATH      =
PLANTUML_CFG_FILE      =
PLANTUML_INCLUDE_PATH  =
DOT_GRAPH_MAX_NODES    = 50
MAX_DOT_GRAPH_DEPTH    = 0
DOT_MULTI_TARGETS      = NO
GENERATE_LEGEND        = YES
DOT_CLEANUP            = YES"""

@cli.command()
@click.option("--name", default=Path.cwd().name, help="The name of the project.")
@click.option("--edition", type=click.Choice(["98", "11", "14", "17", "20", "23", "26"]), default="17", help="The edition (version) of C++ to use.")
@click.option("--docs", type=click.Choice(["none", "doxygen"]), help="The documentation generator to use.")
@click.option("--tests", type=click.Choice(["none", "gtest"]), help="The testing framework to use.")
def init(name, edition, docs, tests):
    # Check that the project name is valid
    valid_characters = [c for c in name if c.islower() or c.isdigit() or c=='-' or c=='_']

    if len(valid_characters) != len(name):
        error("project names can only contain alphanumeric characters, hyphens, and underscores")
        return

    # Check if the current directory is empty
    current_directory = Path(".")

    if any(current_directory.glob("*")):
        error(f"destination `{current_directory.resolve()}` is not empty")
        return

    # Populate via the Pitchfork Layout
    src_directory = Path(current_directory, "src")
    tools_directory = Path(current_directory, "tools")

    src_directory.mkdir() # Source code / header files
    Path(current_directory, "external").mkdir() # Hold third-party libraries
    Path(current_directory, "data").mkdir() # Hold non-code files
    tools_directory.mkdir() # Hold scripts for project management (e.g. build, test, docs)
    tests_directory = Path(current_directory, "tests")

    if tests != "none":
        if tests == "gtest":
            tests_directory.mkdir() # Hold test files

    if docs != "none":
        if docs == "doxygen":
            with (tools_directory / "Doxyfile").open("w", encoding="utf-8") as f:
                f.writelines(generate_doxyfile(name))

    # Create `main.cpp`
    with (src_directory / "main.cpp").open("w", encoding="utf-8") as f:
        f.writelines("""#include <iostream>

int
main() {
    std::cout << "Hello, world!\\n";
    std::cout << "Goodbye, cruel world!\\n";
    
    return 0;
}
""")

    # Create `src/CMakeLists.txt`
    with (src_directory / "CMakeLists.txt").open("w", encoding="utf-8") as f:
        f.writelines(f"""cmake_minimum_required(VERSION 3.24)

project({name} VERSION 1.0
             LANGUAGES CXX)

file(GLOB_RECURSE sources CONFIGURE_DEPENDS "*.cpp")

add_executable(out ${{sources}})

set_target_properties(out PROPERTIES
    CXX_STANDARD {edition}
    CXX_STANDARD_REQUIRED YES
    CXX_EXTENSIONS NO
)""")

    # Create `tests/CMakeLists.txt`
    if tests == "gtest":
        with (tests_directory / "CMakeLists.txt").open("w", encoding="utf-8") as f:
            f.writelines(f"""cmake_minimum_required(VERSION 3.24)

    project({name} VERSION 1.0
                LANGUAGES CXX)

    cmake_policy(SET CMP0135 NEW)

    include(FetchContent)
    FetchContent_Declare(
    googletest
    URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
    )

    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    FetchContent_MakeAvailable(googletest)

    enable_testing()

    file(GLOB_RECURSE sources CONFIGURE_DEPENDS "*.cpp" "../src/*.cpp")
    list(FILTER sources EXCLUDE REGEX "main.cpp")
    add_executable(test_runner ${{sources}})

    set_target_properties(test_runner PROPERTIES
        CXX_STANDARD {edition}
        CXX_STANDARD_REQUIRED YES
        CXX_EXTENSIONS NO
    )

    target_include_directories(test_runner PRIVATE "../src")
    target_link_libraries(
    test_runner
    GTest::gtest_main
    )

    include(GoogleTest)
    gtest_discover_tests(test_runner)
    """)
    
    # Create `build_debug.py`
    with (tools_directory / "build_debug.py").open("w", encoding="utf-8") as f:
        f.writelines("""import pathlib
from pathlib import Path
import subprocess

directory_of_script = Path(__file__).parent.resolve()

subprocess.call(["cmake", "-S", "../src", "-B", "../build/debug"], cwd=directory_of_script)
subprocess.call(["cmake", "--build", "../build/debug"], cwd=directory_of_script)
""")

    # Create `build_release.py`
    with (tools_directory / "build_release.py").open("w", encoding="utf-8") as f:
        f.writelines("""import pathlib
from pathlib import Path
import subprocess

directory_of_script = Path(__file__).parent.resolve()

subprocess.call(["cmake", "-DCMAKE_BUILD_TYPE=Release", "-S", "../src", "-B", "../build/release"], cwd=directory_of_script)
subprocess.call(["cmake", "--build", "../build/release"], cwd=directory_of_script)
""")

    # Create `build_docs.py`
    if docs == "doxygen":
        with (tools_directory / "build_docs.py").open("w", encoding="utf-8") as f:
            f.writelines("""import pathlib
from pathlib import Path
import subprocess

directory_of_script = Path(__file__).parent.resolve()

subprocess.call(["doxygen", "-q"], cwd=directory_of_script)
""")

    # Create `run.py`
    with (tools_directory / "run.py").open("w", encoding="utf-8") as f:
        f.writelines("""import pathlib
from pathlib import Path
import subprocess
import sys

directory_of_script = Path(__file__).parent.resolve()

subprocess.call(["../build/debug/out"], cwd=directory_of_script)
""")

    # Create `build_tests.py`
    if tests == "gtest":
        with (tools_directory / "build_tests.py").open("w", encoding="utf-8") as f:
            f.writelines("""import pathlib
from pathlib import Path
import subprocess

directory_of_script = Path(__file__).parent.resolve()

subprocess.call(["cmake", "-S", "../tests", "-B", "../build/test_runner"], cwd=directory_of_script)
subprocess.call(["cmake", "--build", "../build/test_runner"], cwd=directory_of_script)""")

    # Create `test.py`
    if tests == "gtest":
        with (tools_directory / "test.py").open("w", encoding="utf-8") as f:
            f.writelines("""import pathlib
from pathlib import Path
import subprocess
import sys

directory_of_script = Path(__file__).parent.resolve()

subprocess.call(["../build/test_runner/test_runner"], cwd=directory_of_script)""")

    # Create `.gitignore`
    with (current_directory / ".gitignore").open("w", encoding="utf-8") as f:
        f.writelines("""build""")

    success("created new project")

@cli.command()
@click.option("--debug/--release", default=True)
def build(debug):
    if debug:
        run_build_debug_py()
    else:
        run_build_release_py()

def run_build_debug_py():
    # Check that `build_debug.py` exists
    build_debug_py = Path(".") / "tools/build_debug.py"

    if not build_debug_py.exists():
        error("could not find `build_debug.py` in `./tools`")
        return False
    
    # Run `build_debug.py`
    subprocess.call([sys.executable, build_debug_py])

    success("finished debug build")

    return True

def run_build_release_py():
    # Check that `build_release.py` exists
    build_release_py = Path(".") / "tools/build_release.py"

    if not build_release_py.exists():
        error("could not find `build_release.py` in `./tools`")
        return False
    
    # Run `build_release.py`
    subprocess.call([sys.executable, build_release_py])

    success("finished release build")

    return True

def run_run_py():
    # Check that `run.py` exists
    run_py = Path(".") / "tools/run.py"

    if not run_py.exists():
        error("could not find `run.py` in `./tools`")
        return
    
    # Run `run.py`
    subprocess.call([sys.executable, run_py])

@cli.command()
def run():
    was_found = run_build_debug_py()

    if not was_found:
        return

    # Add a space to separate the build and run outputs
    click.echo()

    run_run_py()

@cli.command()
@click.option("--open", is_flag=True, help="Whether to open the documentation after generating it.")
def docs(open):
    # Check that `build_docs.py` exists
    build_docs_py = Path(".") / "tools/build_docs.py"

    if not build_docs_py.exists():
        error("could not find `build_docs.py` in `./tools`")
        return False
    
    info("generating documentation")

    # Run `build_docs.py`
    subprocess.call([sys.executable, build_docs_py])

    success("documentation generated")

    # Open the documentation if requested
    if open:
        webbrowser.open("file://" + str((Path(".") / "docs/html/index.html").absolute()))

@cli.command()
def test():
    # Check that there are tests
    contents_of_tests_directory = list(Path("tests").iterdir())
    
    if len(contents_of_tests_directory) <= 1: # I.e. it's just CMakeLists.txt
        error("no tests exist to run")
        return
    
    # Check that `build_tests.py` exists
    build_tests_py = Path(".") / "tools/build_tests.py"

    if not build_tests_py.exists():
        error("could not find `build_tests.py` in `./tools`")
        return False
    
    info("building tests")

    # Run `build_tests.py`
    subprocess.call([sys.executable, build_tests_py])

    success("tests built")

    # Check that `test.py` exists
    test_py = Path(".") / "tools/test.py"

    if not test_py.exists():
        error("could not find `test.py` in `./tools`")
        return False
    
    info("running tests")

    # Run `test.py`
    subprocess.call([sys.executable, test_py])

if __name__ == "__main__":
    cli()