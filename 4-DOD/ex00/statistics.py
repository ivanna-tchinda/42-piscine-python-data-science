def ft_mean(args):
    """Calculate the mean."""
    return sum(args) / len(args)


def ft_median(args):
    """Calculate the median."""
    values = sorted(args)
    n = len(values)

    if n % 2 == 0:
        return (values[n // 2 - 1] + values[n // 2]) / 2
    return values[n // 2]


def ft_quartile(args):
    """Calculate the first and third quartiles."""
    values = sorted(args)
    n = len(values)

    q1 = values[int((n - 1) * 0.25)]
    q3 = values[int((n - 1) * 0.75)]

    return [float(q1), float(q3)]


def ft_var(args):
    """Calculate the variance."""
    mean = ft_mean(args)
    return sum((x - mean) ** 2 for x in args) / len(args)


def ft_std(args):
    """Calculate the standard deviation."""
    return ft_var(args) ** 0.5


def ft_statistics(*args, **kwargs):
    """Calculate requested statistics."""
    operations = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_quartile,
        "std": ft_std,
        "var": ft_var
    }

    if len(args) == 0:
        for _ in kwargs:
            print("ERROR")
        return

    for operation_name in kwargs.values():
        if operation_name in operations:
            result = operations[operation_name](args)
            print(f"{operation_name} : {result}")
        else:
            pass