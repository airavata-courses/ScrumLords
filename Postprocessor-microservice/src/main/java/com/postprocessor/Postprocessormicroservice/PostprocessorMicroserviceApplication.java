package com.postprocessor.Postprocessormicroservice;

import java.util.Arrays;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.core.task.TaskExecutor;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;


@SpringBootApplication
@EnableAsync
public class PostprocessorMicroserviceApplication {

	public static void main(String[] args) {
		SpringApplication.run(PostprocessorMicroserviceApplication.class, args);
	}
	
	@Bean
	public CommandLineRunner commandLineRunner(ApplicationContext ctx) {
		return args -> {
			System.out.println("SERVICE IS RUNNING!!!");
			
			//String[] beanNames = ctx.getBeanDefinitionNames();
			//Arrays.parallelSort(beanNames);
			//for (String beanName : beanNames) {
			//	System.out.println(beanName);
			//}
		};
	}
	
	@Bean(name="processExecutor")
    public TaskExecutor workExecutor() {
        ThreadPoolTaskExecutor threadPoolTaskExecutor = new ThreadPoolTaskExecutor();
        threadPoolTaskExecutor.setThreadNamePrefix("Async-");
        threadPoolTaskExecutor.setCorePoolSize(3);
        threadPoolTaskExecutor.setMaxPoolSize(3);
        threadPoolTaskExecutor.setQueueCapacity(600);
        threadPoolTaskExecutor.afterPropertiesSet();
        System.out.println("ThreadPoolTaskExecutor set");
        return threadPoolTaskExecutor;
    }
	

}
