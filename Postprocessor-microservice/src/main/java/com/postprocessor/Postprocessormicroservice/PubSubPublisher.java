package com.postprocessor.Postprocessormicroservice;

import org.springframework.cloud.gcp.pubsub.core.PubSubTemplate;

public abstract class PubSubPublisher {
	
	private final PubSubTemplate pubSubTemplate;
	
	protected PubSubPublisher(PubSubTemplate pubSubTemplate) {
        this.pubSubTemplate = pubSubTemplate;
    }
	
	protected abstract String topic();
	
	public void publish(String message) {
		pubSubTemplate.publish(topic(), message);
	}

}
