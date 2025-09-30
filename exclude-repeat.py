import re

entries  = []
is_repeated_entry = False

def decide_repeated_entry(bib_entry, entries):
    if (bib_entry in entries):
        return False 
    else:
        entries.append(bib_entry)
        return True

with open("bib.bib", "r") as bib_input:
    with open("newbib.bib", "w") as bib_output: 
        for line in bib_input:
            # every entry starts with @
            if line[0] == '@':
                # TOFIX -- This try except is for formatting, It could be resolved simply if one writes a string match for next lines, doing the re.search from the '@' to the first ','
                try:
                    # regular expression from hell to capture the name of the bib entry
                    bib_entry = match = re.search(r"@\w+\{([^,]+),", line).group(1)

                    is_repeated_entry = decide_repeated_entry(bib_entry, entries)
                except:
                    print("The formatting of bib is probably off for this entry. '@' and the name of the entry should be in the same line.")

            # if the flag is up, write the line in the new file
            # if not, ignore it
            if is_repeated_entry:
                bib_output.write(line)
