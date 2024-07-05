type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {

    return async function (...args) {
        return new Promise((resolve, reject) => {
            const timer = setTimeout(() => {
                reject(new Error('Time limit exceeded'));
            }, t);
            fn(...args).then((res) => {
                clearTimeout(timer);
                resolve(res);
            }).catch((err) => {
                clearTimeout(timer);
                reject(err);
            });
        });
    }
};

// Usage
const fn = async (n: number) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(n);
        }, 1000);
    });
};

const fnWithTimeLimit = timeLimit(fn, 500);


fnWithTimeLimit(1).then(console.log).catch(console.error); // Error: Time limit exceeded