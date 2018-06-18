/**
 * Responds to any HTTP request that can provide a "message" field in the body.
 *
 * @param {!Object} req Cloud Function request context.
 * @param {!Object} res Cloud Function response context.
 */

const Datastore = require('@google-cloud/datastore');

// Instantiates a client
const datastore = Datastore();

exports.save_snek = (req, res) => {
  if (req.method === `OPTIONS`) {
	res.set('Access-Control-Allow-Origin', '*')
	   .set('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
       .set('Access-Control-Allow-Headers', 'access-control-allow-origin,content-type,user-agent')
	   .status(200).send();
	   return;
  };
  
    const entity = {
      key: datastore.key('senk'),
      data: req.body
    };

    return datastore.save(entity)
      .then(() => res.status(200)
            .set('Access-Control-Allow-Origin', '*')
            .set('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            .set('Access-Control-Allow-Headers', 'access-control-allow-origin,content-type,user-agent')
            .send(`Entity ${JSON.stringify(entity)} saved.`))
      .catch((err) => {
        console.error(err);
        res.status(500).send(err.message);
        return Promise.reject(err);
      });
};
