'import sys\nfrom greet import greet\n\nif __name__ == "__main__":\n    name = sys.argv[1] if len(sys.argv)  else ""\n    print(greet(name))' 
