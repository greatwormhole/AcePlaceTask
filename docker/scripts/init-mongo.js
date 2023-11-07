users = [
    {
        user: process.env['MONGODB_USERNAME'],
        pwd: process.env['MONGODB_PASSWORD'],
        roles: [
            {
                role: "readWrite",
                db: process.env['MONGO_INITDB_DATABASE']
            },
        ],
        customData: {
            email: process.env['EMAIL'],
            notifications: []
        }
    },
    {
        user: process.env['MONGODB_ADMIN_USERNAME'],
        pwd: process.env['MONGODB_ADMIN_PASSWORD'],
        roles: [
            {
                role: "userAdmin",
                db: process.env['MONGO_INITDB_DATABASE']
            },
        ],
        customData: {
            email: "testdbadmin@example.com",
            notifications: []
        }
    }
]

db.createCollection('testCollection');

for(user of users){
    try{
        db.createUser(user);
    } catch(MongoServerError) {
        continue
    }
}