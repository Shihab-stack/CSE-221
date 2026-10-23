import asyncio
import sys 
async def fetch_data(id , sleep_time):
    print(f"Coroutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id": id , "data":"sample data form coroutine {id}"}


async def main():
    # creating all task corouting and running cocurrently
    
    # results = await asyncio.gather(fetch_data(1,3),fetch_data(2,3) , fetch_data(3,1))
    # a= list(map(str,results))
    # print(" ".join(a)+"\n")
    # task group(built in error handelinh)
    tasks =[]
    async with asyncio.TaskGroup() as tg:
        for i,sleep_time in enumerate([2,1,3], start=1):
            task= tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Recived result:{result} ")













    # print (result_1)
    
    # print(result_2)
    
    # print(result_3)


asyncio.run(main())