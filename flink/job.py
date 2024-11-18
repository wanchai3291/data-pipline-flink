import subprocess
from pyflink.datastream import StreamExecutionEnvironment

def main():
   try:
      env = StreamExecutionEnvironment.get_execution_environment()
      print("Running is working")
      env.set_parallelism(1)

   except Exception as e:
      print(e)


if __name__ == "__main__":
   main()