import sys, getopt # Used to take input for parameters
import os, errno # Used to make directories

def write_file(p_name, path, path_type, c_name, c_type, enum_name, struct_name):
    # print("writing %s file at %s" % (path_type, path))
    
    prefixed_class = c_name
    parent_class = c_type
    if (c_type is ""):
        c_type = "default"
        prefixed_class = "F" + c_name
    elif (c_type in ("Actor", "Pawn", "Character")):
        prefixed_class = "A" + c_name
        c_type = "Actor"
    elif (c_type is "Object" or c_type.find("Component") is not -1):
        prefixed_class = "U" + c_name
        c_type = "Object"
    elif (c_type is "Template"):
        prefixed_class = "T" + c_name
    else:
        prefixed_class = "F" + c_name

    template = ""

    # h file
    if (path_type is "public"):
        print(path + "/" + c_name + ".h Created")
        with open(path + "/" + c_name + ".h", "w") as h:
            with open("./templates/" + c_type + ".h") as h_t:
                template = h_t.read()

                template = template.replace("project_name", p_name.upper())

                template = template.replace("class_name", c_name)
                template = template.replace("prefixed_class", prefixed_class)
                template = template.replace("parent_class", parent_class)

                # h file may have enum
                if (enum_name is not ""):
                    with open("./templates/Enum.txt") as e:
                        e_snippet = e.readlines()
                        enum_acronym = "".join([l for l in enum_name if l.isupper()])

                        for i in range(len(e_snippet)):
                            e_snippet[i] = e_snippet[i].replace("enum_name", enum_name)
                            e_snippet[i] = e_snippet[i].replace("enum_acronym", enum_acronym)

                        enum_header = "".join(e_snippet[:5])
                        e_snippet[7] = "\t" + e_snippet[7]
                        enum_space = "".join(e_snippet[6:])

                        template = template.replace("enum_header", enum_header)
                        template = template.replace("enum_space", enum_space)

                else:
                    template = template.replace("enum_header", "")
                    template = template.replace("enum_space", "")

                # h file may have struct
                if (struct_name is not ""):
                    with open("./templates/Struct.txt") as s:
                        s_snippet = s.read()

                        s_snippet = s_snippet.replace("struct_name", struct_name)

                        template = template.replace("struct_space", s_snippet)
                else:
                    template = template.replace("struct_space", "")

                h.write(template)  

    # cpp file
    if (path_type is "private"):
        print(path + "/" + c_name + ".cpp Created")
        with open(path + "/" + c_name + ".cpp", "w") as cpp:
            with open("./templates/" + c_type + ".cpp") as cpp_t:
                template = cpp_t.read()

                include_path = path[path.find("Private") + 8:]
                template = template.replace("include_path", include_path)

                template = template.replace("class_name", c_name)
                template = template.replace("prefixed_class", prefixed_class)
                template = template.replace("parent_class", parent_class)
                cpp.write(template)



def make_path(path, p_name, add_path, c_name, c_type, enum_name, struct_name):
   # if no project name is provided, exit
    # otherwise, assign project name
    if (p_name is ""):
        print("Need project name")
        sys.exit()
    else:
        path = path.replace("project_name", p_name)
    
    # if no class name is provided, exit
    if (c_name is ""):
        print("Need class name")
        sys.exit()
    
    # add additional path 
    path = path.replace("additional_path", add_path)

    private_path = path.replace("private_or_public", "Private")
    public_path = path.replace("private_or_public", "Public")

    paths = [private_path, public_path]

    for path in paths:
        try:
            os.makedirs(path)
        except OSError as exc:
            print(exc.errno)
            if exc.errno != errno.EEXIST:
                raise
            pass
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s" % path)
    
    # if the directories don't exist, something went wrong.
    if (not os.path.isdir(private_path)):
        print("%s does not exist" % private_path)
        sys.exit()
    if (not os.path.isdir(public_path)):
        print("%s does not exist" % public_path)
        sys.exit()
    
    # check whether the .h and .cpp file already exist, and override them if prompted by the user
    private_file_path = private_path + "/" + c_name + ".cpp"
    public_file_path = public_path + "/" + c_name + ".h"
    if (os.path.isfile(private_file_path)):
        override_h = input(".h file already exists.\nDo you wish to override it? Y/N\n")
        if (override_h is "N"):
            sys.exit()
        else:
            print("Removing .h file to override...\n")
            os.remove(private_file_path)
            write_file(p_name, private_path, "private", c_name, c_type, enum_name, struct_name)
    else:
        write_file(p_name, private_path, "private", c_name, c_type, enum_name, struct_name)

    if (os.path.isfile(public_file_path)):
        override_cpp = input(".cpp file already exists.\nDo you wish to override it? Y/N\n")
        if (override_h is "N"):
            sys.exit()
        else:
            print("Removing .cpp file to override...\n")
            os.remove(public_file_path)
            write_file(p_name, public_path, "public", c_name, c_type, enum_name, struct_name)
    else:
        write_file(p_name, public_path, "public", c_name, c_type, enum_name, struct_name)


def regenerate_project_files(regen_path):
    current = os.getcwd
    os.chdir("/mnt/d/Epic Games/UE_4.24/Engine/Binaries/DotNET")
    os.system("./UnrealBuildTool.exe -projectfiles -project='%s' -game -rocket -progress" % regen_path)


def main(argv):
    # output files
    cpp = ''
    h = ''

    # path template
    path = "../WIP/MyGames/project_name/Source/project_name/private_or_public/additional_path"

    # varialbes to fill the template
    project_name = ""
    additional_path = ""
    class_name = ""
    class_type = ""
    enum_name = ""
    struct_name = ""

    # input parameters
    try: 
        opts, args = getopt.getopt(argv, "hp:d:c:t:e:s:")
    except getopt.GetoptError:
        print("CppMaker.py -p <project name> -d <desired/directory> -c <class name> -t <class type> -e <enum name> -s <struct name>\n -p and -c are required")    
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("CppMaker.py -p <project name> -d <desired/directory> -c <class name> -t <class type> -e <enum name> -s <struct name>\n -p and -c are required")    
            sys.exit()
        elif opt in ("-p"):
            project_name = arg
        elif opt in ("-d"):
            additional_path = arg
        elif opt in ("-c"):
            class_name = arg
        elif opt in ("-t"):
            class_type = arg
        elif opt in ("-e"):
            enum_name = arg
        elif opt in ("-s"):
            struct_name = arg
            
    
    make_path(path, project_name, additional_path, class_name, class_type, enum_name, struct_name)

    # path including D:/Dev/UE4 is perferred by UE4
    path = "D:/Dev/UE4/WIP/MyGames/project_name/Source/project_name/private_or_public/additional_path"
    regen_path = path.replace("project_name/Source/project_name/private_or_public/additional_path", project_name + "/" + project_name + ".uproject")
    regenerate_project_files(regen_path)

if __name__ == "__main__":
    main(sys.argv[1:])