package test;
import java.util.*;
public class bench {
	public static final long MEGA = 1048576;
	public static final double KILO = 1000.0;
	public static final int NUM_ITERATIONS = 200000000;
	public static final int QUANTUM = 1000000;
	public static final int MAX_ARRAY_SIZE = 40000000;
	public static void main(String[] args) {
		System.gc();
		ArrayList<Integer>arr = new ArrayList<Integer>();
		
		long initialMemoryUsed = (long)Math.round((Runtime.getRuntime().totalMemory()-Runtime.getRuntime().freeMemory())/MEGA);
		long startTime = System.currentTimeMillis();
		long current = -1, currentTime = -1, maxMemory = -1, previousTime = startTime;
		double utilization = 0;
		System.out.println("T(ms)\tMem(MB)\tAvg.M.U.(MB)");
		for(int i = 0; i < NUM_ITERATIONS;i++) {
			arr.add(i);
			if(i% QUANTUM == 0) {
				current = (long)Math.round((Runtime.getRuntime().totalMemory()-Runtime.getRuntime().freeMemory())/MEGA);
				maxMemory = (current>maxMemory)?current:maxMemory;
				currentTime = System.currentTimeMillis();
				utilization += (currentTime -previousTime)*(current-initialMemoryUsed)/KILO;
				System.out.printf("%d\t%d\t%8.3f\n",
						(currentTime-startTime),current-initialMemoryUsed,
						KILO*utilization/(currentTime-startTime));
				previousTime = currentTime;
			}
			if(i% MAX_ARRAY_SIZE == 0)
				while(!arr.isEmpty()) {
					
					arr.remove(arr.size()-1);
					if(arr.size() % QUANTUM == 0) {
						currentTime = System.currentTimeMillis();
						current = (long)Math.round((Runtime.getRuntime().totalMemory()-Runtime.getRuntime().freeMemory())/MEGA);
						maxMemory = (current>maxMemory)?current:maxMemory;
						utilization += (currentTime -previousTime)*(current-initialMemoryUsed)/KILO;
						System.out.printf("%d\t%d\t%8.3f\n",
								(currentTime-startTime),
								current-initialMemoryUsed,
								KILO*utilization/(currentTime-startTime)
								);
						previousTime = currentTime;
						//System.gc();
					}
				}
			
		}
		System.out.println("Total time is "+(System.currentTimeMillis()-startTime)/KILO+" seconds, memory usage peak was "
				+maxMemory+"MB and Memory Utilization is "+utilization+"(MB.seconds).");		
	}
}