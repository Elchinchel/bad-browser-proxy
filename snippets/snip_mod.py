result = su("snip_mod_replacer", read_snippet(args[0]))
write_snippet(args[0], result)
r = "Done"