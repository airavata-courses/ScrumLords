package com.postprocessor.Postprocessormicroservice;

import java.util.Map;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;



@Service
public class Postprocessor implements PostProcessService {
	/*
	private final long id;
	private final String content;
	
	public Postprocessor(long id, String content) {
		this.id = id;
		this.content = content;
		
	}
	
	public long getId() {
		return id;
	}
	
	public String getContent() {
		return content;
	}
	
	*/
	
	//@Async
	@Override
	@Async("processExecutor")
	public void getProcessedData(Map<String, Object> data) {
		try {
			System.out.println("Sleep state!");
			Thread.sleep(15 * 1000);
			System.out.println("Sleep state complete!");
			System.out.println(data);
		}
		catch (Exception e) {
			System.out.println("Error in getProcessedData.");
		}
	}

	@Override
	public void getProcessedData() {
		// TODO Auto-generated method stub
		
	}

	
}
