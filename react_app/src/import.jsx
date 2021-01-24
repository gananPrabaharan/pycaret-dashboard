import React, { useState } from "react"
import { Container , Form, Row, Col } from "react-bootstrap"
import { SERVER, SESSION_ID, getRequestOptions } from "./util"
import Table from "./table"
import { importTableColumns } from "./tableColumns"
import axios from 'axios'

const ImportWizard = (props) => {
    const [state, setState] = useState({
        featureList: [],
        targetFeature: "-1",
        error: false
    });

    const handleFileChange = async (e) => {
        const file = e.target.files[0];
        let formData = new FormData();
        formData.append("fileInput", file);
        formData.append("sessionId", JSON.stringify(SESSION_ID))

        const options = getRequestOptions(formData);
        const url = SERVER + "api/upload/";

        axios.post(url, formData, options)
            .then((response)=>{
                setState({...state, featureList: response.data, error: false});
            }).catch((error) => {
                console.error(error);
                setState({...state, error: true})
            });
    }

    const setFeatureList = (featureList) => {
        setState({...state, featureList: featureList});
    }

    const onTargetSelect = (e) => {
        setState({...state, targetFeature: e.target.value});
    }

    const importConfig = () => {
        const url = SERVER + "/api/feature_config";
        let formData = new FormData();
        formData.append("sessionId", SESSION_ID);
        formData.append("featureDictList", state.featureList);

        const options = getRequestOptions(formData);

        axios.post(url, options)
            .then((response) => {
                setState({...state, error: false});
            }).catch((error) => {
                console.error(error);
                setState({...state, error: true})
            });
    }

    return(
        <Container fluid>
            <div style={{margin:"3%"}}>
                <Form method="post" action="import" encType="multipart/form-data">
                    <Form.Group>
                        <Row>
                            <Col sm={5}>
                                <Form.Label>Select Dataset CSV:</Form.Label>
                                <Form.File id="fileInput" accept=".csv" onChange={(e) => handleFileChange(e)}/>
                            </Col>
                        </Row>
                    </Form.Group>
                    <Table dataList={ state.featureList } columns={ importTableColumns } changeStateData={ setFeatureList } />
                    <Form.Group style={{margin:"1rem 0 2rem 0"}}>
                        <Row>
                            <Col sm={3}>
                                <Form.Label>Select Target Feature:</Form.Label>
                                <Form.Control as="select" value={state.targetFeature}
                                    onChange={(e)=>onTargetSelect(e)}>
                                    <option value="-1" disabled>Select Target Feature</option>
                                    {
                                        state.featureList.filter(feature => feature["include"]==="Yes").map(opt => {
                                            return <option value={opt["name"]} key={opt["name"]}>{opt["name"]}</option>
                                        })
                                    }
                                </Form.Control>
                            </Col>
                        </Row>
                    </Form.Group>
                    <Form.Group style={{margin:"1rem 0 3rem 0"}}>
                        <Row>
                            <Col sm={2}>
                                <Form.Control type="button" value="Import" className="outline-dark center-block"
                                onClick={ importConfig }/>
                            </Col>
                        </Row>
                    </Form.Group>
                </Form>
            </div>
        </Container>
    )

}

export default ImportWizard