package com.postprocessor.Postprocessormicroservice;

import java.io.FileWriter;
import java.io.InputStream;
import java.lang.reflect.Type;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import javax.swing.JFrame;

import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.google.api.core.ApiFuture;
import com.google.api.core.ApiFutureCallback;
import com.google.api.core.ApiFutures;
import com.google.api.gax.core.CredentialsProvider;
import com.google.api.gax.core.NoCredentialsProvider;
import com.google.api.gax.grpc.GrpcTransportChannel;
import com.google.api.gax.rpc.FixedTransportChannelProvider;
import com.google.api.gax.rpc.TransportChannelProvider;
import com.google.cloud.pubsub.v1.Publisher;
import com.google.cloud.pubsub.v1.TopicAdminClient;
import com.google.cloud.pubsub.v1.TopicAdminSettings;
import com.google.common.util.concurrent.MoreExecutors;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.google.protobuf.ByteString;
import com.google.pubsub.v1.ProjectTopicName;
import com.google.pubsub.v1.PubsubMessage;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;




@Service
public class Postprocessor implements PostProcessService {
	
	
	private final HelloPubSubPublisher publisher;
	
	@Value("${spring.cloud.gcp.pubsub.emulator-host}")
	private String hostportvalue;
	
	@Value("${spring.cloud.gcp.project-id}")
	private String projectid;
	
	@Value("${spring.cloud.gcp.topic-id}")
	private String topicid;
	
	@Value("${openweather.api.key}")
	private String apikey;
	
	@Autowired
    public Postprocessor(HelloPubSubPublisher publisher) {
        this.publisher = publisher;
    }
	
	//@Async
	@Override
	@Async("processExecutor")
	public void getProcessedData(Map<String, Object> data) {
		try {
			
			System.out.println("JSON OBJECT TEST");
			
			Map<String, Object> hourly = (Map<String, Object>) data.get("hourly");
			Map<String, Object> currently = (Map<String, Object>) data.get("currently");
			Map<String, Object> daily = (Map<String, Object>) data.get("daily");
			ArrayList<String> alerts =  (ArrayList<String>) data.get("alerts");
			
			
			System.out.println("Writing Summary for data!");
			
			//String data_str = data.toString();
			
			//String[] all_timestamps = StringUtils.substringsBetween(data_str, "time=", ",");
			//String[] all_summary = StringUtils.substringsBetween(data_str, "summary=", "");
			
			//Double lat = Double.parseDouble(data.get("latitude").toString());
			//Double lon = Double.parseDouble(data.get("longitude").toString());
			
			//int lat = Integer.parseInt(data.get("latitude").toString());
			//int lon = Integer.parseInt(data.get("longitude").toString());
			
			//int lat = 2;
			//int lon = 2;
			/*
			final String url = "https://tile.openweathermap.org/map/precipitation_new/2/"+lat+"/"+lon+".png?appid="+apikey;
			
			final String url2 = "https://tilecache.rainviewer.com/v2/radar/1581213000/512/2/"+lat+"/"+lon+"/1/0_0.png";
			
			final String url3 = "https://tilecache.rainviewer.com/v2/composite/1581220800/8192/0/0_1.png";
			
			System.out.println(url3);
			System.out.println("Weather api call start.");
			
			
			try(InputStream in = new URL(url3).openStream()){
			    Files.copy(in, Paths.get("image.png"));
			}
			
			
			*/
			
			/*
			RestTemplate restTemplate = new RestTemplate();
			byte[] result = restTemplate.getForObject(url3, byte[].class);
			Files.write(Paths.get("image.png"), result);
			*/
			
			//System.out.println("Weather api call end.");
			//System.out.println(result);
			
			
			
			
			//System.out.println(hourly_data);
			
			String hourly_data = hourly.get("data").toString();
			String[] time_hourly = StringUtils.substringsBetween(hourly_data, "time=", ",");
			String[] summary_hourly = StringUtils.substringsBetween(hourly_data, "summary=", ",");
			
			String currently_data = currently.toString();
			String[] time_currently = StringUtils.substringsBetween(currently_data, "time=", ",");
			String[] summary_currently = StringUtils.substringsBetween(currently_data, "summary=", ",");
			
			String daily_data = daily.get("data").toString();
			String[] time_daily = StringUtils.substringsBetween(daily_data, "time=", ",");
			String[] summary_daily = StringUtils.substringsBetween(daily_data, "summary=", ",");
			
			String alerts_data = alerts.toString();
			String[] alerts_title = StringUtils.substringsBetween(alerts_data, "title=", ",");
			String[] alerts_regions = StringUtils.substringsBetween(alerts_data, "regions=", "],");
			String[] alerts_severity = StringUtils.substringsBetween(alerts_data, "severity=", ",");
			String[] alerts_desc = StringUtils.substringsBetween(alerts_data, "description=", ", uri=");
			
			System.out.println(alerts_data);
			
			String summary_string = "-----SUMMARY AFTER DATA ANALYSIS----- \n \n \n";
			
			summary_string = summary_string + "CURRENT DAY SUMMARY:-> \n \n";
			
			if (time_currently != null && summary_currently != null) {
				for (int i = 0; i < time_currently.length; i++) {
					java.util.Date time = new java.util.Date((long)Integer.parseInt(time_currently[i])*1000);
					String time_str = time.toString();
					summary_string = summary_string + time_str + " : " + summary_currently[i] + "\n"; 
				}
			}
			
			summary_string = summary_string + "\nHOURLY SUMMARY:-> \n \n";
			
			if (time_hourly != null && summary_hourly != null) {
				for (int i = 0; i < time_hourly.length; i++) {
					java.util.Date time = new java.util.Date((long)Integer.parseInt(time_hourly[i])*1000);
					String time_str = time.toString();
					summary_string = summary_string + time_str + " : " + summary_hourly[i] + "\n"; 
				}
			}
			
			summary_string = summary_string + "\nDAILY SUMMARY:-> \n \n";
			
			if (time_daily != null && summary_daily != null) {
				for (int i = 0; i < time_daily.length; i++) {
					java.util.Date time = new java.util.Date((long)Integer.parseInt(time_daily[i])*1000);
					String time_str = time.toString();
					summary_string = summary_string + time_str + " : " + summary_daily[i] + "\n"; 
				}
			}
			
			summary_string = summary_string + "\nALERTS SUMMARY:-> \n \n";
			
			if (alerts_title != null && alerts_regions != null && alerts_severity != null && alerts_desc != null) {
				for (int i = 0; i < alerts_title.length; i++) {
					summary_string = summary_string + alerts_title[i] + "\nSeverity:  " + alerts_severity[i] + "\nRegions affected: " + alerts_regions[i] + "\nDescription: " + alerts_desc[i] + "\n"; 
				}
			}
			
			summary_string = summary_string + "\n \n ---END OF SUMMARY---";
			
			System.out.println("Writing summary to file");
			FileWriter file = new FileWriter("data_files/summary.txt");
			file.write(summary_string);
			file.close();
			System.out.println("Summary File write completed");
			
			/*
			ArrayList<Double> int_temp = new ArrayList<Double>();
			
			if (hourly_temps != null) {
			for(String temp : hourly_temps) {
				if (temp != null) {
				int_temp.add(Double.parseDouble(temp));
				}
			}
			}
			
			ArrayList<Integer> int_time = new ArrayList<Integer>();
			
			for (int i=0; i<=24; i++) {
				int_time.add(i);
			}
			
			System.out.println("PRINTING HOURLY DATA");
			for (int i=0; i<=24; i++) {
				System.out.println(int_temp.get(i) + "--- " + int_time.get(i));
			}
			
			System.out.println("Creating plot!!!");
			
			*/
			
			System.out.println("Sleep state!");
			Thread.sleep(5 * 1000);
			System.out.println("Sleep state complete!");
			System.out.println(data);
			
			System.out.println("Converting to json");
			Gson gson = new Gson();
			Type gsonType = new TypeToken<HashMap>(){}.getType();
			
			String gsonString = gson.toJson(data, gsonType);
			System.out.println(gsonString);
			
			System.out.println("Writing to file");
			FileWriter file1 = new FileWriter("data.json");
			file1.write(gsonString);
			file1.close();
			System.out.println("File write completed");
			
			System.out.println("Sending message to pubsub");
			
			String hostport = hostportvalue;
			System.out.println("HOSTPORT: " + hostport);
			ManagedChannel channel = ManagedChannelBuilder.forTarget(hostport).usePlaintext().build();
			try {
			  TransportChannelProvider channelProvider =
			      FixedTransportChannelProvider.create(GrpcTransportChannel.create(channel));
			  CredentialsProvider credentialsProvider = NoCredentialsProvider.create();

			  // Set the channel and credentials provider when creating a `TopicAdminClient`.
			  // Similarly for SubscriptionAdminClient
			  TopicAdminClient topicClient =
			      TopicAdminClient.create(
			          TopicAdminSettings.newBuilder()
			              .setTransportChannelProvider(channelProvider)
			              .setCredentialsProvider(credentialsProvider)
			              .build());

			  ProjectTopicName topicName = ProjectTopicName.of(projectid, topicid);
			  // Set the channel and credentials provider when creating a `Publisher`.
			  // Similarly for Subscriber
			  Publisher publisher =
			      Publisher.newBuilder(topicName)
			          .setChannelProvider(channelProvider)
			          .setCredentialsProvider(credentialsProvider)
			          .build();
			  
			  String topic = publisher.getTopicNameString();
			  System.out.println("TOPIC: " + topic);
			  
			  //String message = "my_message";
			  ByteString data1 = ByteString.copyFromUtf8(gsonString);
			  PubsubMessage pubsubMessage = PubsubMessage.newBuilder().setData(data1).build();
			  ApiFuture<String> messageIdFuture = publisher.publish(pubsubMessage);
			  
			  
			  
			  ApiFutures.addCallback(messageIdFuture, new ApiFutureCallback<String>() {
				   public void onSuccess(String messageId) {
				     System.out.println("published with message id: " + messageId);
				   }

				   public void onFailure(Throwable t) {
				     System.out.println("failed to publish: " + t);
				   }
				 }, MoreExecutors.directExecutor());
			  
			} finally {
			  //channel.shutdown();
			}
			System.out.println("Message sent to pubsub");
		}
		catch (Exception e) {
			System.out.println("Error in getProcessedData.");
			e.printStackTrace();
		}
	}

	private Publisher getPublisher() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void getProcessedData() {
		
	}

	
}
