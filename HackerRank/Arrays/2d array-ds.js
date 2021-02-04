

function CreateProgram(props){

    const [program, setProgram] = useState({
        name: "",
        length: 0,
        description: "",
        user_id: 0
    
    })
    
        useEffect(() => {
            setProgram({...program, user_id: props.user_id})
        }, [props.user_id]); 
    
        const changeHandler = event => { 
            setProgram({...program, [event.target.name]: event.target.value})
        }
       console.log(props.user_id)
    return (
        <>
            <h1>Create Your Workout Program</h1>
            <form >
                <label>Program Name</label>
                <input 
                    name ="name"
                    value= {program.name}
                    required
                    placeholder = "Enter Name here"
                    onChange = {changeHandler}
                />
                <label>Length</label>
                <input 
                    name ="length"
                    type = {Number}
                    value= {program.length}
                    required
                    placeholder = "how long"
                    onChange = {changeHandler}
                />
                <label>Program Description</label>
                <input 
                    name ="description"
                    value= {program.description}
                    onChange = {changeHandler}
                    placeholder = "Enter description here"
                />
    
            
    
        </form>
        <Link to = "/dashboard"><button>back</button></Link>
        </>
    )
    }
    const mapStateToProps = state => {
        return {
            user_id: state.user_id
        }
    }
    
    
    export default connect(
        mapStateToProps, {}
    )(CreateProgram)