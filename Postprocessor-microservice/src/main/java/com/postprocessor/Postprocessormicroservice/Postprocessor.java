package com.postprocessor.Postprocessormicroservice;

import java.io.FileWriter;
import java.lang.reflect.Type;
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
			
			String hourly_data = hourly.get("data").toString();
			
			System.out.println(hourly_data);
			
			String[] hourly_temps = StringUtils.substringsBetween(hourly_data, "temperature=", ",");
			
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
			FileWriter file = new FileWriter("data.json");
			file.write(gsonString);
			file.close();
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
