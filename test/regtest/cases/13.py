
filedata="""

<!--# set ( { "foo" => ( 1, ( "bar", 4, ( "biz" ) ) ),
              "baz" => ( 10, 20, 30),
              "bar" => 10 } ) -->

{$ set { x : 10,
         y : [ 20, 180, "hello", "bye", "adios" ],
         z : [ 1, [2, [3, [4, [5, "final" ] ] ] ] ] } $}
"""

display = [ ("foo.0", 1),
            ("foo.1.0", "bar"),
            ("foo.1.1", 4),
            ("foo.1.2.0", "biz"),
            ("baz.0", 10),
            ("baz.1", 20),
            ("baz.2", 30),
            ("bar", 10),
            ("x", 10),
            ("y.0", 20),
            ("y.1", 180),
            ("y.2", "hello"),
            ("y.3", "bye"),
            ("z.0", 1),
            ("z.1.0", 2),
            ("z.1.1.0", 3),
            ("z.1.1.1.0", 4),
            ("z.1.1.1.1.1", "final") ]

script_path = "configtest?fn=$[0]&display=" + \
    ','.join ([p[0] for p in display])

outcome= "\n".join (["%s -> %s" % p for p in display ])

