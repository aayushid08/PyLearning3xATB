# real example of tuple

# env variables kabhi change nahi hote to yaha tuples ka use kar skate hai

ENV_API_URLs = (
    "abc.com/get",
    "vgj.com/post",
    "ppooii.com/ push"
)
print(ENV_API_URLs)

ENV_API_URLs = tuple (
    ["abc.com/get",
    "vgj.com/post",
    "ppooii.com/ push"]
)
print(ENV_API_URLs)

