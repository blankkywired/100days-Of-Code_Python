def pass_fail(score):
    if score > 50:
        result = "Passed"
        return result
    else:
        result = "Failed"
        return result

print(pass_fail(50))