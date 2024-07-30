import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};

// Create a job in the push_notification_code queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.log('Notification job failed to create');
    }
  });

// Job completion handler
job.on('complete', () => {
  console.log('Notification job completed');
});

// Job failure handler
job.on('failed', () => {
  console.log('Notification job failed');
});
