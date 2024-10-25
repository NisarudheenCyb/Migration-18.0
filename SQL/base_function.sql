CREATE OR REPLACE FUNCTION manage_records()
RETURNS void LANGUAGE plpgsql AS
$$
BEGIN
    -- Delete from report_layout and ir_ui_view tables
    DELETE FROM report_layout;
    DELETE FROM ir_ui_view;

    -- Select query (you can modify this part if you need to return the results)
    PERFORM * FROM rule_group_rel WHERE group_id = 11;

    -- Delete and update in rule_group_rel
    DELETE FROM rule_group_rel WHERE group_id = 11;
    UPDATE rule_group_rel SET group_id = 2 WHERE group_id = 11;

    -- Delete from ir_model where model matches
    DELETE FROM ir_model WHERE model LIKE '%ir.server.object.lines%';

    -- Drop table if it exists
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'ir_server_object_lines') THEN
        EXECUTE 'DROP TABLE ir_server_object_lines;';
    END IF;
END;
$$;

________________________________________________________________________________________________________________________


