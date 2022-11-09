from pdttools.exceptions import PdttoolsFunctionalException


def print_dict(the_dict, output_file=None):
    import json
    if output_file is None:  # pragma: no cover
        print(json.dumps(the_dict, indent=4))
    else:
        with open(output_file, "w") as f:
            json.dump(the_dict, f, indent=4)


def print_array(the_list, output_file=None, format="pretty", column_names=None, max_column_width=None):
    # Do something only if there is at least one item in the list
    if len(the_list) == 0:
        return

    # Convert list elements of object type into a dictionary type
    for i in range(len(the_list)):
        if not isinstance(the_list[i], dict):
            try:
                the_list[i] = vars(the_list[i])
            except TypeError as e:
                raise PdttoolsFunctionalException("Item at line " + str(i) + " is not consistent: " + str(the_list[i])) from None

    # Computing column_names in case it is None, meaning all columns.
    if column_names is None:
        column_names = list(the_list[0].keys())
        for adict in the_list:
            for key in adict.keys():
                if key not in column_names:
                    column_names.append(key)

    # Setting a special string for undefined field
    for adict in the_list:
        for column_name in column_names:
            if column_name not in adict.keys():
                adict[column_name] = "<field not defined>"

    # List printing algorithmn
    def to_pretty_format(file):
        from contextlib import redirect_stdout

        with redirect_stdout(f):
            # 1) Evaluate width of all columns
            col_width = {i: len(i) for i in column_names}
            for adict in the_list:
                for column_name, value in adict.items():
                    if column_name in column_names:
                        value = str(value)
                        if len(value) > col_width[column_name]:
                            col_width[column_name] = len(value)

            # 2) Determine what column to hide because of 'max_column_width' parameter
            hidden_columns = []
            for column_name in column_names:
                if (max_column_width is not None and col_width[column_name] > max_column_width):
                    hidden_columns.append(column_name)

            # 3) Printing columns name
            for column_name in column_names:
                if column_name not in hidden_columns:
                    print("{:{width}}".format(column_name, width=col_width[column_name]), end=" ")
            print("")

            # 4) Printing a line below the column name
            for column_name in column_names:
                if column_name not in hidden_columns:
                    print("-" * col_width[column_name], end=" ")
            print("")

            # 5) Printing all rows
            for adict in the_list:
                for column_name in column_names:
                    value = adict.get(column_name)
                    value = str(value)
                    if column_name not in hidden_columns:
                        print("{:{width}}".format(value, width=col_width[column_name]), end=" ")
                print("")

    def to_csv_format(file):
        import csv
        writer = csv.DictWriter(file, fieldnames=column_names, delimiter=";")
        writer.writeheader()
        for result in the_list:
            writer.writerow(result)

    if format == "pretty":
        if output_file is None:  # pragma: no cover
            import sys
            to_pretty_format(file=sys.stdout)
        else:
            with open(output_file, "w") as f:
                to_pretty_format(file=f)
    if format == "csv":
        if output_file is None:  # pragma: no cover
            import sys
            to_csv_format(file=sys.stdout)
        else:
            with open(output_file, "w", newline="") as csvfile:
                to_csv_format(file=csvfile)
