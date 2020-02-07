package com.postprocessor.Postprocessormicroservice;

import java.io.FileWriter;
import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;



@Service
public class Postprocessor implements PostProcessService {
	
	private final HelloPubSubPublisher publisher;
	
	@Autowired
    public Postprocessor(HelloPubSubPublisher publisher) {
        this.publisher = publisher;
    }
	
	//@Async
	@Override
	@Async("processExecutor")
	public void getProcessedData(Map<String, Object> data) {
		try {
			System.out.println("Sleep state!");
			Thread.sleep(15 * 1000);
			System.out.println("Sleep state complete!");
			System.out.println(data);
			
			System.out.println("Converting to json");
			Gson gson = new Gson();
			Type gsonType = new TypeToken<HashMap>(){}.getType();
			
			String gsonString = gson.toJson(data, gsonType);
			System.out.println(gsonString);
			
			System.out.println("Writing to file");
			FileWriter file = new FileWriter("data.json");
			file.write(gsonString);
			file.close();
			System.out.println("File write completed");
			
			System.out.println("Sending message to pubsub");
			
			publisher.publish("Test Message from post processor microservice");
			System.out.println("Message sent to pubsub");
		}
		catch (Exception e) {
			System.out.println("Error in getProcessedData.");
		}
	}

	@Override
	public void getProcessedData() {
		
	}

	
}
