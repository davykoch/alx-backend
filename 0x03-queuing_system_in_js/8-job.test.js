import { expect } from 'chai';
import kue from 'kue';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });

  it('should display correct log messages', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];

    const consoleSpy = sinon.spy(console, 'log');

    createPushNotificationsJobs(jobs, queue);

    setTimeout(() => {
      expect(consoleSpy.calledWith(sinon.match(/Notification job created: \d+/))).to.be.true;

      queue.testMode.jobs[0].emit('complete');
      queue.testMode.jobs[0].emit('failed', new Error('Job failed'));
      queue.testMode.jobs[0].emit('progress', 50);

      expect(consoleSpy.calledWith(sinon.match(/Notification job \d+ completed/))).to.be.true;
      expect(consoleSpy.calledWith(sinon.match(/Notification job \d+ failed: Error: Job failed/))).to.be.true;
      expect(consoleSpy.calledWith(sinon.match(/Notification job \d+ 50% complete/))).to.be.true;

      consoleSpy.restore();
      done();
    }, 50);
  });
});
